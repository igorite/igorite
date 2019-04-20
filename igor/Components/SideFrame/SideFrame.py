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
from PyQt5.QtWidgets import QFrame, QSplitter, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from igor.Components.SideFrame.DataTree import DataTree
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
        self.tree_container.hide_title()
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
        self.title = SideFrameTitleFrame(title)
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

    def __init__(self, title):
        # ----------------------------------
        # Initialize Frame and Variables
        # ----------------------------------

        QFrame.__init__(self)
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
        # Create Button
        # ----------------------------------

        self.close_button = QPushButton()
        self.close_button.setMaximumSize(QSize(20, 20))
        self.layout.addWidget(self.close_button)
