from PyQt5.QtWidgets import QTabWidget
from igor.Gui.TestFrame.TestPanel import TestPanel
from igor.Gui.TestFrame.TestTextEditor import TestTextEditor
from igor.Gui.TestFrame.StepsEditor import StepsEditor
from igor.Gui.TestFrame.MyEditor import TextEdit


class TestTabPanel(QTabWidget):

    def __init__(self, test_data):
        QTabWidget.__init__(self)
        self.addTab(TextEdit(test_data,self), 'Steps')

