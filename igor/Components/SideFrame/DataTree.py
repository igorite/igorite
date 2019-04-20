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


# ----------------------------------
# Imports
# ----------------------------------
import os
from os import path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu, QAction
from robot.api import TestData
from robot.libraries import BuiltIn, OperatingSystem, Process, String, Remote, Telnet, Collections, Screenshot, XML
from robot.parsing.model import TestCaseFile, TestCase, TestDataDirectory
from igor.Gui.StyleSheet import style_sheet
from igor.Components.images.Images import Images
# ----------------------------------


class DataTree(QTreeWidget):

    def __init__(self,
                 parent,
                 root_name,
                 show_test=False,
                 show_variable=False,
                 show_keyword=False,
                 show_libraries=False):
        # ----------------------------------
        # Initialize class and variables
        # ----------------------------------

        QTreeWidget.__init__(self)
        self.side_frame = parent
        self.root_name = root_name
        self.main_frame = parent.main_frame
        self.show_test = show_test
        self.show_variable = show_variable
        self.show_keyword = show_keyword
        self.show_libraries = show_libraries
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_dict = {}
        self.id = 0
        self.root = None
        self.source = None
        self.libraries = None
        self.font = QFont()
        # ----------------------------------
        # Configure Tree
        # ----------------------------------
        self.setHeaderHidden(True)
        self.itemDoubleClicked.connect(self.item_clicked_open)

        # ----------------------------------
        # Configure Font
        # ----------------------------------
        self.font.setPointSize(13)
        self.setFont(self.font)

    def open_project(self, project_path):
        """
        This function open a project and fill the Tree with data
        :param project_path: project path
        :type project_path: str
        :return: None
        """
        self.clear()
        self.open_directory(project_path)
        if self.show_libraries:
            self.add_libraries()

    def open_directory(self, file_path):
        self.source = TestData(source=file_path)
        self.root = QTreeWidgetItem()
        self.root.setText(0, self.root_name)
        self.root.setIcon(0, Images.APP_ICON)

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
            if isinstance(children, TestDataDirectory):
                child = FolderWidget(children)
            if isinstance(children, TestCaseFile):
                child = FileWidget(children)
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
        child = TestWidget(test)
        child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        child.setCheckState(0, Qt.Unchecked)
        child.setText(0, test.name)
        root.addChild(child)

    def add_keyword(self, keyword, root):
        self.test_dict[keyword.name] = keyword
        child = KeywordWidget(keyword)
        child.setText(0, keyword.name)
        root.addChild(child)

    def add_library_keyword(self, keyword, root):
        self.test_dict[keyword] = keyword
        text = keyword.replace('_', ' ')
        text = text.title()
        child = KeywordWidget(keyword)
        child.setText(0, text)
        root.addChild(child)

    def add_variable(self, variable, root):
        self.test_dict[variable.name] = variable
        child = TestWidget(variable)
        child.setText(0, variable.name)
        root.addChild(child)

    def item_clicked_open(self, item):
        if isinstance(self.test_dict[item.text(0)], TestCase):
            self.main_frame.main_panel.open_tab(self.test_dict[item.text(0)])
        else:
            pass

    def add_libraries(self):

        # TODO: add DATE and Time and Messages
        default_libraries = [[BuiltIn.BuiltIn, 'Built In'],
                             [OperatingSystem.OperatingSystem, 'Operating System'],
                             [Process.Process, 'Process'],
                             [String.String, 'String'],
                             [Remote.Remote, 'Remote'],
                             [Telnet.Telnet, 'Telnet'],
                             [Collections.Collections, 'Collections'],
                             [Screenshot.Screenshot, 'ScreenShot'],
                             [XML.XML, 'XML']]

        self.libraries = LibraryFolderWidget()
        self.libraries.setText(0, 'Libraries')
        self.addTopLevelItem(self.libraries)

        for library in default_libraries:
            library_root = LibraryWidget()
            library_root.setText(0, library[1])
            self.libraries.addChild(library_root)
            for func in self.import_library(library[0]):
                self.add_library_keyword(func, library_root)

    @staticmethod
    def import_library(library):
        return [func for func in dir(library) if not func.startswith('_')]

    def contextMenuEvent(self, event):
        if event.reason() == event.Mouse:

            item = self.itemAt(event.pos())
            if isinstance(item, TestWidget):
                TestMenu(self, event, item)
            if isinstance(item, FileWidget):
                TestFileMenu(self, event, item)


class TestMenu(QMenu):

    def __init__(self,parent, event, item):
        """

                :type parent: DataTree
                :param event:
                :type item: TestWidget
                """

        QMenu.__init__(self)
        self.tree = parent
        self.event = event
        self.item = item
        self.setStyleSheet(style_sheet)

        create_file = QAction('Rename')
        self.addAction(create_file)

        delete_file = QAction('Delete test case')
        delete_file.setIcon(Images.DELETE_ICON)
        delete_file.triggered.connect(self.delete)
        self.addAction(delete_file)

        self.action = self.exec_(self.mapToGlobal(event.pos()))

    def delete(self):
        test = self.item.test_data
        test_table = self.item.test_data.parent
        test_file = self.item.test_data.parent.parent

        self.item.parent().removeChild(self.item)
        test_table.tests.remove(test)
        test_file.save()


class TestFileMenu(QMenu):

    def __init__(self, parent, event, item):
        """

        :type parent: DataTree
        :param event:
        :param item:
        """
        QMenu.__init__(self)
        self.tree = parent
        self.event = event
        self.item = item
        self.setStyleSheet(style_sheet)

        create_file = QAction('Create Test')
        create_file.triggered.connect(self.add_test)
        self.addAction(create_file)

        delete_file = QAction('Delete File')
        delete_file.triggered.connect(self.delete)
        self.addAction(delete_file)

        self.action = self.exec_(self.mapToGlobal(event.pos()))

    def delete(self):
        test = self.item.test_data
        print(test.source)
        print(test)

    def add_test(self):
        test_file = self.item.test_data
        test_file_test_table = self.item.test_data.testcase_table
        test = test_file_test_table.add('hola')
        test_file.save()
        self.tree.add_test_case(test, self.item)


class TestWidget(QTreeWidgetItem):

    def __init__(self, test_data):
        QTreeWidgetItem.__init__(self)
        self.test_data = test_data
        self.setIcon(0, Images.TEST_ICON)


class KeywordWidget(QTreeWidgetItem):

    def __init__(self, test_data):
        QTreeWidgetItem.__init__(self)
        self.test_data = test_data
        self.setIcon(0, Images.KEYWORD_ICON)


class VariableWidget(QTreeWidgetItem):

    def __init__(self, test_data):
        QTreeWidgetItem.__init__(self)
        self.test_data = test_data
        self.setIcon(0, Images.VARIABLE_ICON)


class FolderWidget(QTreeWidgetItem):

    def __init__(self, test_data):
        QTreeWidgetItem.__init__(self)
        self.test_data = test_data
        self.setIcon(0, Images.FOLDER_ICON)


class FileWidget(QTreeWidgetItem):

    def __init__(self, test_data):
        QTreeWidgetItem.__init__(self)
        self.test_data = test_data
        self.setIcon(0, Images.TEST_CASE_FILE_ICON)


class LibraryFolderWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)
        self.setIcon(0, Images.LIBRARIES_ICON)


class LibraryWidget(QTreeWidgetItem):

    def __init__(self):
        QTreeWidgetItem.__init__(self)
        self.setIcon(0, Images.PYTHON_ICON)