import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, \
    QTabWidget, QVBoxLayout, QAction, QToolBar, QPlainTextEdit, QTableWidget, QTableWidgetItem
from robot.parsing.model import TestCase
from igor.Gui.SideFrame import SideFrame
from igor.Gui.StyleSheet import style_sheet


class MainWindow(QMainWindow):

    def __init__(self, ):
        QMainWindow.__init__(self)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Igor')
        self.setStyleSheet(style_sheet)
        self.showMaximized()
        self.main_frame = MainFrame()
        self.setCentralWidget(self.main_frame)
        self.toolbar = self.addToolBar(Toolbar(self))
        self.path = os.path.abspath(path.dirname(__file__))
        self.setWindowIcon(QIcon(path.join(self.path, 'images', 'IgorIcon.png')))

    def run_tests(self):
        # runner = self.main_frame.main_panel.open_runner()
        # robot_run = RobotRun(self.main_frame.side_frame.tree.source.source)
        pass


class Toolbar(QToolBar):

    def __init__(self, parent):
        self.parent = parent
        QToolBar.__init__(self)
        self.setMovable(False)
        self.path = os.path.abspath(path.dirname(__file__))
        self.play = QAction(QIcon(path.join(self.path, 'images', 'Play.png')), 'Run', self)
        self.play.triggered.connect(self.parent.run_tests)
        self.addAction(self.play)


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

        self.addTab(TestPanel(robot_data), self.test_icon, robot_data.name)
        if self.count() >= 1:
            self.setTabsClosable(True)

    def open_runner(self):
        self.runner = Runner()
        self.addTab(self.runner, self.test_icon, 'Run')
        return self.runner

    def welcome_tab(self):
        self.addTab(QFrame(), self.test_icon, 'Open')


class TestPanel(QFrame):

    def __init__(self, test_data):
        """

        :param test_data:
         :type test_data: TestCase
        """
        self.test_data = test_data
        print(type(test_data))
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        step_container = StepsContainer(test_data, self)
        self.layout.addWidget(step_container)


class StepsContainer(QFrame):

    def __init__(self, test_case, parent):
        """

        :param test_case:
        :type test_case: TestCase
        """
        QFrame.__init__(self)
        self.parent = parent
        self.test_case = test_case
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.steps_table = QTableWidget()
        self.steps_table.alternatingRowColors()
        self.steps_table.setRowCount(5)
        self.steps_table.setColumnCount(20)
        self.steps_table.setMinimumSize(80, 800)
        self.layout.addWidget(self.steps_table)
        self.add_steps()

    def add_steps(self):
        i = 0
        for step in self.test_case.steps:
            print(step)
            sed = QTableWidgetItem()
            sed.setText(step.name)
            self.steps_table.setItem(i, 0, sed)
            i += 1


class Runner(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.stream = QPlainTextEdit()
        self.stream.setObjectName('stream')
        # self.stream.setEnabled(False)
        self.layout.addWidget(self.stream, 0, Qt.AlignCenter)

    def add_text(self, text):
        self.stream.appendPlainText(text)
