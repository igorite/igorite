import os
from os import path

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QFrame, QSplitter, QHBoxLayout, QTreeWidget, QTreeWidgetItem, \
    QTabWidget, QVBoxLayout, QAction, QToolBar, QPlainTextEdit, QTableWidget, QTableWidgetItem, QLabel, QPushButton
from igor.Gui.SideFrame.TestTree import TestTree
from igor.Gui.SideFrame.KeywordTree import KeywordTree


class SideFrame(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)
        self.main_frame = parent

        self.test_tree = TestTree(self)
        self.keyword_tree = KeywordTree(self)
        self.tree_container = SideFrameContainer(self.test_tree, 'Test cases')
        self.keyword_tree_container = SideFrameContainer(self.keyword_tree, 'Keywords')
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
