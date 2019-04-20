# Copyright 2019 SocIsomer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, \
    QTabWidget, QAction, QToolBar, QPlainTextEdit, QMessageBox, QFileDialog
from igor.Components.Core.RobotRun import RobotRun
from igor.Components.Project import *
from igor.Components.Git.GitShowLog import GitLogWindow
from igor.Components.Project.CreateProjectWindow import CreateProjectWindow
from igor.Components.SideFrame.SideFrame import SideFrame
from igor.Components.TestFrame.TestTabPanel import TestTabPanel
from igor.Gui.StyleSheet import style_sheet
from igor.Components.Core.Configuration import Config


class MainWindow(QMainWindow):

    def __init__(self, project_path=None):
        QMainWindow.__init__(self)
        self.path = os.path.abspath(path.dirname(__file__))
        self.setGeometry(800, 300, 300, 300)
        self.setWindowTitle('Igorite')
        self.project_path = project_path

        self.app_icon = QIcon(os.path.join(self.path, '..', 'components', 'images', 'IgorIcon.png'))
        self.folder_icon = QIcon(os.path.join(self.path, '..', 'components', 'images', 'folder_icon.png'))
        self.play_icon = QIcon(os.path.join(self.path, '..', 'components', 'images', 'play.png'))

        self.setWindowIcon(self.app_icon)

        self.setStyleSheet(style_sheet)
        self.main_frame = MainFrame(self)
        self.setCentralWidget(self.main_frame)
        # self.toolbar = self.addToolBar(Toolbar(self))
        self.robot_run = None
        self.load = None
        self.run_options = None
        self.menu = None
        self.project_window = None
        self.git_manager = None
        self.pop_up = None
        self.add_menu()
        self.font = QFont()
        self.set_app_font()

        self.showMaximized()

    def run_tests(self):
        runner = self.main_frame.main_panel.open_runner()
        self.robot_run = RobotRun(self.main_frame.side_frame.test_tree.source.source)
        self.robot_run.signal.connect(runner.add_text)
        self.robot_run.start()

    def open_run_tests(self):
        pass

    def add_menu(self):
        self.menu = self.menuBar()
        # File Menu
        file_menu = self.menu.addMenu('File')

        create_project_action = QAction('New Project', file_menu)
        create_project_action.setShortcut('Ctrl+N')
        create_project_action.triggered.connect(self.create_project)
        file_menu.addAction(create_project_action)

        load_project_action = QAction('Load Project', file_menu)
        load_project_action.setIcon(self.folder_icon)
        load_project_action.setShortcut('Ctrl+O')
        load_project_action.triggered.connect(self.load_project)
        file_menu.addAction(load_project_action)

        # Git Menu
        git_menu = self.menu.addMenu('Git')
        git_action = QAction('Show log', file_menu)
        git_action.setShortcut('Ctrl+S')
        git_action.triggered.connect(self.git_show_log)
        git_menu.addAction(git_action)

        # Run Menu

        run_menu = self.menu.addMenu('Run')
        run_action = QAction('Run tests', run_menu)
        run_action.setIcon(self.play_icon)
        run_action.setShortcut('Ctrl+R')
        run_action.triggered.connect(self.run_tests)
        run_menu.addAction(run_action)

    def create_project(self):
        self.project_window = CreateProjectWindow()

    def load_project(self):
        self.pop_up = QFileDialog()
        self.pop_up.setFileMode(QFileDialog.DirectoryOnly)
        self.pop_up.fileSelected.connect(self.load_project_data)
        self.pop_up.show()

    def load_project_data(self, directory_path):
        self.main_frame.side_frame.update_project_data(directory_path)
        Config().load_configuration(directory_path)

    def git_show_log(self):
        self.git_manager = GitLogWindow()

    def set_app_font(self):
        font_id = QFontDatabase.addApplicationFont(path.join(path.dirname(self.path),
                                                             'components',
                                                             'font',
                                                             'FiraCode-Medium.ttf'))
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font.setPointSize(12)
        self.font.setFamily(family)
        self.setFont(self.font)

    @staticmethod
    def closeEvent(event, **kwargs):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplemented the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        :param event:
        """
        close_window = QMessageBox()
        reply = close_window.question(close_window,
                                      "Message",
                                      "Are you sure you want to quit? Any unsaved work will be lost.",
                                      close_window.Save | close_window.Close | close_window.Cancel,
                                      )

        if reply:
            pass


class Toolbar(QToolBar):

    def __init__(self, parent):
        self.parent = parent
        QToolBar.__init__(self)
        self.setMovable(False)
        self.path = os.path.abspath(path.dirname(__file__))
        # Create Play button
        self.play = QAction(QIcon(path.join(self.path, 'images', 'Play.png')), 'Run', self)
        self.play.triggered.connect(self.parent.run_tests)
        self.addAction(self.play)
        # Create Run button
        self.run_button = QAction(QIcon(path.join(self.path, 'images', 'Play.png')), 'Run', self)
        self.run_button.triggered.connect(self.parent.open_run_tests)
        self.addAction(self.run_button)


class MainFrame(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)
        self.window = parent

        splitter = QSplitter(Qt.Horizontal)
        self.side_frame = SideFrame(self)
        self.main_panel = MainPanel()
        splitter.addWidget(self.side_frame)
        splitter.addWidget(self.main_panel)
        splitter.setSizes([150, 600])

        layout = QHBoxLayout(self)
        layout.setStretch(0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(splitter)
        self.setLayout(layout)


class MainPanel(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_icon = QIcon(path.join(self.path, '..', 'Components', 'images', 'test_icon.png'))
        self.setMovable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.runner = None
        self.welcome_tab()

    def close_tab(self, p_int):
        if self.count() <= 2:
            self.setTabsClosable(False)
        self.removeTab(p_int)

    def open_tab(self, robot_data):

        self.addTab(TestTabPanel(robot_data), self.test_icon, robot_data.name)
        self.setCurrentIndex(self.count()-1)
        if self.count() >= 1:
            self.setTabsClosable(True)

    def open_runner(self):
        self.runner = Runner()
        self.addTab(self.runner, self.test_icon, 'Run')
        self.setCurrentIndex(self.count() - 1)
        if self.count() >= 1:
            self.setTabsClosable(True)
        return self.runner

    def welcome_tab(self):
        self.addTab(WelcomeTab(), self.test_icon, 'Open')


class Runner(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.stream = QPlainTextEdit()
        self.stream.setObjectName('stream')
        # self.stream.setEnabled(False)
        self.layout.addWidget(self.stream)

    def add_text(self, text):
        self.stream.appendPlainText(text)
