import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from robot.api import TestData
from robot.parsing.model import TestCaseFile


class TestTree(QTreeWidget):

    def __init__(self, parent):
        self.side_frame = parent
        self.main_frame = parent.main_frame
        QTreeWidget.__init__(self)
        self.setHeaderHidden(True)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_dict = {}
        self.id = 0
        self.root = None
        self.source = None
        self.suite_icon = QIcon(path.join(self.path, '..', 'images', 'folder_icon.png'))
        self.test_icon = QIcon(path.join(self.path, '..', 'images', 'test_icon.png'))

        self.open_directory()
        self.itemDoubleClicked.connect(self.item_clicked_open)
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

    def open_directory(self, filepath=None):
        self.source = TestData(source='C:\\Users\\3l1n\\Desktop\\RobotDemo-master')
        self.root = QTreeWidgetItem()
        self.root.setText(0, self.source.name)
        self.root.setFlags(self.root.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsTristate)
        self.get_child_suites(self.source, self.root)
        self.addTopLevelItem(self.root)
        self.root.setExpanded(True)

    def get_child_suites(self, suite, root):
        for children in suite.children:
            self.test_dict[children.name] = children
            child = QTreeWidgetItem()
            if isinstance(children, TestCaseFile):
                child.setIcon(0, self.suite_icon)
            child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            child.setCheckState(0, Qt.Unchecked)
            child.setText(0, children.name)
            if children.children or children.testcase_table:
                self.get_child_suites(children, child)
            root.addChild(child)
        for test in suite.testcase_table:
            self.test_dict[test.name] = test
            child = TestTreeWidget()
            child.setIcon(0, self.test_icon)
            child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            child.setCheckState(0, Qt.Unchecked)
            child.setText(0, test.name)
            root.addChild(child)

    def item_clicked_open(self, item):
        if self.test_dict[item.text(0)]:
            self.main_frame.main_panel.open_tab(self.test_dict[item.text(0)])
        else:
            pass


class TestTreeWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)
