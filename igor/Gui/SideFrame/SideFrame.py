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


from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFrame, QSplitter, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from igor.Gui.SideFrame.DataTree import TestTree


class SideFrame(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)
        self.main_frame = parent

        self.test_tree = TestTree(self, 'Project', show_test=True, show_variable=True, show_keyword=True)
        self.keyword_tree = TestTree(self, 'Objects', show_keyword=True, show_variable=True)
        self.tree_container = SideFrameContainer(self.test_tree, 'Test cases')
        self.keyword_tree_container = SideFrameContainer(self.keyword_tree, 'Keywords')
        self.keyword_tree_container.hide_title()
        self.tree_container.hide_title()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSizeConstraint(0)
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.tree_container)
        self.splitter.addWidget(self.keyword_tree_container)

        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

    def get_tree(self):
        return self.tree


class SideFrameContainer(QFrame):

    def __init__(self, widget, title):
        QFrame.__init__(self)

        self.widget = widget
        self.title = SideFrameTitleFrame(title)

        self.layout = QVBoxLayout()
        self.layout.setSizeConstraint(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)

    def hide_title(self):
        self.title.hide()


class SideFrameTitleFrame(QFrame):

    def __init__(self, title):
        QFrame.__init__(self)
        self.label = QLabel(title)
        self.close_button = QPushButton()
        self.close_button.setMaximumSize(QSize(20, 20))

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)
