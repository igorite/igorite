import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from robot.api import TestData
from robot.parsing.model import TestCaseFile, TestCase


class TestTree(QTreeWidget):

    def __init__(self, parent, show_test=False, show_variable=False, show_keyword=False):
        self.side_frame = parent
        self.main_frame = parent.main_frame
        self.show_test = show_test
        self.show_variable = show_variable
        self.show_keyword = show_keyword

        QTreeWidget.__init__(self)
        self.setHeaderHidden(True)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_dict = {}
        self.id = 0
        self.root = None
        self.source = None
        self.suite_icon = QIcon(path.join(self.path, '..', 'images', 'folder_icon.png'))
        self.test_icon = QIcon(path.join(self.path, '..', 'images', 'test_icon.png'))
        self.keyword_icon = QIcon(path.join(self.path, '..', 'images', 'keyword_icon.png'))
        self.variable_icon = QIcon(path.join(self.path, '..', 'images', 'variable_icon.png'))

        self.open_directory()

        self.itemDoubleClicked.connect(self.item_clicked_open)
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

    def open_directory(self, filepath='C:\\Users\\3l1n\\Desktop\\RobotDemo-master'):
        self.source = TestData(source=filepath)
        self.root = QTreeWidgetItem()
        self.root.setText(0, self.source.name)
        self.root.setFlags(self.root.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsTristate)

        self.get_child_data(self.source,
                            self.root,
                            tests_data=self.show_test,
                            keywords_data=self.show_keyword,
                            variable_data=self.show_variable)

        self.addTopLevelItem(self.root)
        self.root.setExpanded(True)

    def get_child_data(self,
                       suite,
                       root,
                       tests_data=False,
                       keywords_data=False,
                       variable_data=False
                       ):
        for children in suite.children:
            self.test_dict[children.name] = children
            child = QTreeWidgetItem()
            if isinstance(children, TestCaseFile):
                child.setIcon(0, self.suite_icon)
            child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            child.setCheckState(0, Qt.Unchecked)
            child.setText(0, children.name)
            if children.children or children.testcase_table:
                self.get_child_data(children, child, tests_data, keywords_data, variable_data)
            root.addChild(child)

        if tests_data:
            for test in suite.testcase_table:
                self.add_test_case(test, root)

        if keywords_data:
            for keyword in suite.keyword_table:
                self.add_keyword(keyword, root)
        if variable_data:
            for variable in suite.variable_table:
                self.add_variable(variable, root)

    def add_test_case(self, test, root):
        self.test_dict[test.name] = test
        child = TestTreeWidget()
        child.setIcon(0, self.test_icon)
        child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        child.setCheckState(0, Qt.Unchecked)
        child.setText(0, test.name)
        root.addChild(child)

    def add_keyword(self, keyword, root):
        self.test_dict[keyword.name] = keyword
        child = KeywordTreeWidget()
        child.setIcon(0, self.keyword_icon)
        child.setText(0, keyword.name)
        root.addChild(child)

    def add_variable(self, variable, root):
        self.test_dict[variable.name] = variable
        child = TestTreeWidget()
        child.setIcon(0, self.variable_icon)
        child.setText(0, variable.name)
        root.addChild(child)

    def item_clicked_open(self, item):
        if isinstance(self.test_dict[item.text(0)],TestCase):
            self.main_frame.main_panel.open_tab(self.test_dict[item.text(0)])
        else:
            pass


class TestTreeWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)

class KeywordTreeWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)