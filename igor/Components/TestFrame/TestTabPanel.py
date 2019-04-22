from PyQt5.QtWidgets import QTabWidget
from igor.Components.TestFrame.MyEditor import TextEditorFrame


class TestTabPanel(QTabWidget):

    def __init__(self, test_data):
        QTabWidget.__init__(self)
        self.addTab(TextEditorFrame(test_data), 'Steps')
