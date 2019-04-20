# Copyright 2019 Igorite
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

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFrame, QSplitter, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTreeWidgetItemIterator
from igor.Components.SideFrame.DataTree import DataTree, KeywordWidget, TestWidget, VariableWidget
from igor.Components.images.Images import Images
# ----------------------------------


class SideFrame(QFrame):

    def __init__(self, parent):
        # ----------------------------------
        # Initialize Frame and Variables
        # ----------------------------------

        QFrame.__init__(self)
        self.main_frame = parent
        self.window = parent.window
        self.project_path = parent.window.project_path
        # ----------------------------------
        # Create Layout Manager
        # ----------------------------------

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSizeConstraint(0)
        self.setLayout(self.layout)
        # ----------------------------------
        # Create Splitter Manager
        # ----------------------------------

        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.setSizes([1000, 0])
        self.layout.addWidget(self.splitter)
        # ----------------------------------
        # Create Data Trees
        # ----------------------------------

        self.test_tree = DataTree(self,
                                  'Project',
                                  show_test=True,
                                  show_variable=True,
                                  show_keyword=True,
                                  show_libraries=True)
        self.tree_container = SideFrameContainer(self.test_tree, 'Test cases')
        # self.tree_container.hide_title()
        self.splitter.addWidget(self.tree_container)
        # ----------------------------------

        self.keyword_tree = DataTree(self, 'Objects', show_keyword=True, show_variable=True)
        self.keyword_tree_container = SideFrameContainer(self.keyword_tree, 'Keywords')
        self.keyword_tree_container.hide_title()
        self.splitter.addWidget(self.keyword_tree_container)
        # ----------------------------------
        # Fill Data Trees
        # ----------------------------------
        self.splitter.setSizes([1000, 0])

        if self.project_path:
            self.test_tree.open_project(self.project_path)

    def get_tree(self):
        return self.tree

    def update_project_data(self, project_path):
        self.test_tree.open_project(project_path)


class SideFrameContainer(QFrame):

    def __init__(self, widget, title):
        # ----------------------------------
        # Initialize Frame and Variables
        # ----------------------------------

        QFrame.__init__(self)
        self.widget = widget
        self.title = SideFrameTitleFrame(self.widget, title)
        # ----------------------------------
        # Create Layout Manager
        # ----------------------------------

        self.layout = QVBoxLayout()
        self.layout.setSizeConstraint(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # ----------------------------------
        # Add Widgets
        # ----------------------------------

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.widget)

    def hide_title(self):
        """
        This function hides the title bar of the Tree Container
        :return: None
        """
        self.title.hide()


class SideFrameTitleFrame(QFrame):

    def __init__(self, tree, title):
        # ----------------------------------
        # Initialize Frame and Variables
        # ----------------------------------

        QFrame.__init__(self)
        self.tree = tree
        # ----------------------------------
        # Create Layout Manager
        # ----------------------------------

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        # ----------------------------------
        # Create Title
        # ----------------------------------

        self.label = QLabel(title)
        self.layout.addWidget(self.label)
        # ----------------------------------
        # Create Show buttons
        # ----------------------------------

        self.keywords_button = CustomCheckBox(Images.KEYWORD_ICON, Images.KEYWORD_HIDE_ICON, self.show_keywords)
        self.keywords_button.setMaximumSize(QSize(30, 30))
        self.layout.addWidget(self.keywords_button)
        # ----------------------------------

        self.test_button = CustomCheckBox(Images.TEST_ICON, Images.TEST_HIDE_ICON, self.show_tests)
        self.test_button.setMaximumSize(QSize(20, 20))
        self.layout.addWidget(self.test_button)
        # ----------------------------------

        self.variable_button = CustomCheckBox(Images.VARIABLE_ICON, Images.VARIABLE_HIDE_ICON, self.show_variables)
        self.variable_button.setMaximumSize(QSize(20, 20))
        self.layout.addWidget(self.variable_button)
        # ----------------------------------

    def show_keywords(self):
        if self.keywords_button.is_checked():
            self.hide_items(KeywordWidget)
        else:
            self.show_items(KeywordWidget)

    def show_variables(self):
        if self.variable_button.is_checked():
            self.hide_items(VariableWidget)
        else:
            self.show_items(VariableWidget)

    def show_tests(self):
        if self.test_button.is_checked():
            self.hide_items(TestWidget)
        else:
            self.show_items(TestWidget)

    def hide_items(self, item_type):
        iterator = QTreeWidgetItemIterator(self.tree, QTreeWidgetItemIterator.NotHidden)

        while iterator.value() is not None:
            if isinstance(iterator.value(), item_type):
                iterator.value().setHidden(True)

            iterator += 1

    def show_items(self, item_type):
        iterator = QTreeWidgetItemIterator(self.tree, QTreeWidgetItemIterator.Hidden)

        while iterator.value() is not None:
            if isinstance(iterator.value(), item_type):
                iterator.value().setHidden(False)

            iterator += 1


class CustomCheckBox(QPushButton):

    def __init__(self, checked_icon, unchecked_icon, function):
        QPushButton.__init__(self)
        self.checked = False
        self.checked_icon = checked_icon
        self.unchecked_icon = unchecked_icon
        self.function = function
        self.setIcon(self.checked_icon)
        self.clicked.connect(self.connect)

    def connect(self):
        if self.checked:
            self.checked = False
            self.setIcon(self.checked_icon)
        else:
            self.checked = True
            self.setIcon(self.unchecked_icon)
        self.function()

    def is_checked(self):
        return self.checked
