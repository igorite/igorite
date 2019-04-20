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


import sys
import json
import traceback
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import qFatal
from igor.Gui.main import MainWindow
from igor.Components.Core.Configuration import Config, MainFont
from igor.Components.images.Images import Images


class BootLoader:

    def __init__(self):

        self.window = None
        self.app = None
        self.configuration = None
        sys.excepthook = self.excepthook

        self.start_application()

        self.load_configuration()

        self.open_project()

        self.load_main_window()

        sys.exit(self.window.exec_())

    def open_project(self):
        pass

    def load_configuration(self):

        with open(os.path.join(os.path.dirname(__file__), 'default.json')) as json_file:
            self.configuration = json.load(json_file)
        config = Config()
        config.load_configuration()
        self.window.setFont(MainFont.FONT)

    def load_main_window(self):
        self.app = MainWindow(Config.CURRENT_PROJECT_PATH)

    def start_application(self):
        self.window = QApplication([])



    @staticmethod
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        qFatal('')
