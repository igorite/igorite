from igor.Gui.PopUpWindows.PopUp import PopUpWindow
from PyQt5.QtWidgets import QFrame


class CreateProjectWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self, 'Load Project')
        self.show()


class CreateProjectFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self)
