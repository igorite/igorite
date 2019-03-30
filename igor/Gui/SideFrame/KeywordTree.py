import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, QTreeWidget, QTreeWidgetItem, \
    QTabWidget, QVBoxLayout, QAction, QToolBar, QPlainTextEdit, QTableWidget, QTableWidgetItem, QLabel, QPushButton
from robot.api import TestData
from robot.parsing.model import TestCaseFile, TestCase


class KeywordTree(QTreeWidget):

    def __init__(self, parent):
        self.side_frame = parent
        self.main_frame = parent.main_frame
        QTreeWidget.__init__(self)
        self.setHeaderHidden(True)
        self.setAnimated(True)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_dict = {}
        self.id = 0
        self.root = None
        self.source = None
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

        self.suite_icon = QIcon(path.join(self.path, '..', 'images', 'icon.png'))
        self.test_icon = QIcon(path.join(self.path, '..', 'images', 'keyword_icon.png'))

        self.open_directory()

    def open_directory(self, filepath=None):
        self.source = TestData(source='C:\\Users\\3l1n\\Desktop\\RobotDemo-master')
        self.root = QTreeWidgetItem()
        self.root.setText(0, self.source.name)
        self.root.setText(1, 'hola')
        self.root.setFlags(self.root.flags())
        self.get_child_suites(self.source, self.root)
        self.addTopLevelItem(self.root)
        self.root.setExpanded(True)

    def get_child_suites(self, suite, root):
        for children in suite.children:
            self.test_dict[children.name] = children
            child = QTreeWidgetItem()
            if isinstance(children, TestCaseFile):
                child.setIcon(0, self.suite_icon)
            child.setFlags(child.flags())
            child.setText(0, children.name)
            if children.children or children.testcase_table:
                self.get_child_suites(children, child)
            root.addChild(child)
        for test in suite.keyword_table:
            self.test_dict[test.name] = test
            child = FolderTreeWidget()
            child.setIcon(0, self.test_icon)
            child.setFlags(child.flags())
            child.setText(0, test.name)
            root.addChild(child)


class TestTreeWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)


class FolderTreeWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)