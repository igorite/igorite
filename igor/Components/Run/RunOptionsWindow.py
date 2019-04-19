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

from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout
from igor.Components.Core.PopUp import PopUpWindow
from igor.Gui.StyleSheet import style_sheet


class RunOptionsWindow(PopUpWindow):

    def __init__(self):
        # ----------------------------------
        # Initialize window
        # ----------------------------------

        PopUpWindow.__init__(self, 'Hola')
        self.setStyleSheet(style_sheet)
        # ----------------------------------
        # Create layout manager
        # ----------------------------------

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        # ----------------------------------
        # Add main window widget
        # ----------------------------------

        self.layout.addWidget(RunOptionsWindowPanel())
        # ----------------------------------
        # show Window
        # ----------------------------------

        self.show()


class RunOptionsWindowPanel(QFrame):

    def __init__(self):
        # ----------------------------------
        # Initialize window
        # ----------------------------------

        QFrame.__init__(self)
        # ----------------------------------
        # Create layout manager
        # ----------------------------------

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        # ----------------------------------
        # add widgets
        # ----------------------------------
        self.label = QLabel('hola')
        self.layout.addWidget(self.label)
