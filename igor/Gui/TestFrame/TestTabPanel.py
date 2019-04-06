from PyQt5.QtWidgets import QTabWidget
from igor.Gui.TestFrame.TestPanel import TestPanel
from igor.Gui.TestFrame.TestTextEditor import TestTextEditor


class TestTabPanel(QTabWidget):

    def __init__(self, test_data):
        QTabWidget.__init__(self)
        self.addTab(TestPanel(test_data), 'Grid')
        self.addTab(TestTextEditor(), 'Test Editor')
