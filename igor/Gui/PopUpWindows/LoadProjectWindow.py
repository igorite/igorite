from igor.Components.Core.PopUp import PopUpWindow
from PyQt5.QtWidgets import QFrame


class LoadProjectWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self, 'Load Project')
        self.show()


class LoadProjectFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self)
