import sys
import json
import traceback
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import qFatal
from igor.Gui.main import MainWindow


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

    def load_main_window(self):
        self.app = MainWindow()

    def start_application(self):
        self.window = QApplication([])

    @staticmethod
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        qFatal('')
