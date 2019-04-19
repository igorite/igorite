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
from os import path
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from igor.Gui.StyleSheet import style_sheet


class PopUpWindow(QWidget):

    def __init__(self, title):
        QWidget.__init__(self)
        self.path = os.path.abspath(path.dirname(__file__))
        self.project_icon = QIcon(path.join(self.path, '..', 'images', 'IgorIcon.png'))
        self.setWindowIcon(self.project_icon)
        self.setWindowTitle(title)
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet(style_sheet)

    def center_window(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())