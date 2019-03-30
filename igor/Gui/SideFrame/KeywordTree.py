import os
from os import path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, QTreeWidget, QTreeWidgetItem, \
    QTabWidget, QVBoxLayout, QAction, QToolBar, QPlainTextEdit, QTableWidget, QTableWidgetItem, QLabel, QPushButton
from robot.api import TestData
from robot.parsing.model import TestCaseFile, TestCase


class KeywordTree(QTreeWidget):

    def __init__(self, parent):
        self.side_frame = parent
        self.main_frame = parent.main_frame
        QTreeWidget.__init__(self)
        self.setHeaderHidden(True)
        self.path = os.path.abspath(path.dirname(__file__))
        self.test_dict = {}
        self.id = 0
        self.root = None
        self.source = None
