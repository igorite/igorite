from PyQt5.QtWidgets import QWidget
from igor.Gui.StyleSheet import style_sheet


class PopUpWindow(QWidget):

    def __init__(self, title):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet(style_sheet)