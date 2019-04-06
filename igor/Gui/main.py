import os
import ctypes
from os import path

from PyQt5.QtCore import Qt , QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, \
    QTabWidget, QAction, QToolBar, QPlainTextEdit, QSystemTrayIcon
from igor.Core.RobotRun import RobotRun
from igor.Gui.PopUpWindows.LoadProjectWindow import LoadProjectWindow
from igor.Gui.PopUpWindows.RunOptionsWindow import RunOptionsWindow
from igor.Gui.SideFrame.SideFrame import SideFrame
from igor.Gui.StyleSheet import style_sheet
from igor.Gui.TestFrame.TestTabPanel import TestTabPanel


class MainWindow(QMainWindow):

    def __init__(self, ):
        QMainWindow.__init__(self)
        self.path = os.path.abspath(path.dirname(__file__))
        self.setGeometry(800, 300, 300, 300)
        self.setWindowTitle('Dánao')

        self.app_icon = QIcon(os.path.join(self.path, 'images', 'IgorIcon.png'))

        self.setWindowIcon(self.app_icon)
        trayIcon = QSystemTrayIcon(self.app_icon)
        trayIcon.show()


        self.setStyleSheet(style_sheet)
        self.main_frame = MainFrame()
        self.setCentralWidget(self.main_frame)
        self.toolbar = self.addToolBar(Toolbar(self))
        self.robot_run = None
        self.load = None
        self.run_options = None
        self.menu = None
        self.add_menu()
        self.showMaximized()

    def run_tests(self):
        runner = self.main_frame.main_panel.open_runner()
        self.robot_run = RobotRun(self.main_frame.side_frame.test_tree.source.source)
        self.robot_run.signal.connect(runner.add_text)
        self.robot_run.start()

    def open_run_tests(self):
        self.run_options = RunOptionsWindow()

    def add_menu(self):
        self.menu = self.menuBar()
        # File Menu
        file_menu = self.menu.addMenu('File')

        load_project_action = QAction('Load Project', file_menu)
        load_project_action.setShortcut('Ctrl+O')
        load_project_action.triggered.connect(self.load_project)
        file_menu.addAction(load_project_action)

        # Create Run menu
        run_menu = self.menu.addMenu('Run')

        # Create help menu
        help_menu = self.menu.addMenu('Help')

    def load_project(self):
        self.load = LoadProjectWindow()


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

    def __init__(self):
        QFrame.__init__(self)

        splitter = QSplitter(Qt.Horizontal)
        self.side_frame = SideFrame(self)
        self.main_panel = MainPanel()
        splitter.addWidget(self.side_frame)
        splitter.addWidget(self.main_panel)
        splitter.setSizes([100, 600])

        layout = QHBoxLayout(self)
        layout.setStretch(0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(splitter)
        self.setLayout(layout)


class MainPanel(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_icon = QIcon(path.join(self.path, 'images', 'test_icon.png'))
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
        self.addTab(QFrame(), self.test_icon, 'Open')


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
