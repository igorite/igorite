import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget, QLabel
from robot.api import TestData
from robot.parsing.model import TestCaseFile


class PopUpWindow(QWidget):

    def __init__(self, title):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.setGeometry(300, 300, 300, 300)