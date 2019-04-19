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
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QToolButton
import os
# ----------------------------------


class WelcomeTab(QFrame):

    def __init__(self):
        # ----------------------------------
        # Initiliaze Frame and Variables
        # ----------------------------------

        QFrame.__init__(self)
        self.path = os.path.abspath(os.path.dirname(__file__))

        # ----------------------------------
        # Create Layout Manager
        # ----------------------------------
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # ----------------------------------
        # Create Font
        # ----------------------------------
        self.font = QFont()
        self.font.setPointSize(16)

        # ----------------------------------
        # Create open project button
        # ----------------------------------
        self.open_button = QToolButton()
        self.open_button.setFont(self.font)
        self.open_button.setText('Open Project')
        self.open_button.setIcon(QIcon(os.path.join(self.path, 'images', 'new_icon.png')))
        self.open_button.setIconSize(QSize(200, 200))
        self.open_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.layout.addWidget(self.open_button)

        # ----------------------------------
        # Create create project button
        # ----------------------------------
        self.create_button = QToolButton()
        self.create_button.setFont(self.font)
        self.create_button.setText('Create Project')
        self.create_button.setIcon(QIcon(os.path.join(self.path, 'images', 'variable_icon.png')))
        self.create_button.setIconSize(QSize(200, 200))
        self.create_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.layout.addWidget(self.create_button)
