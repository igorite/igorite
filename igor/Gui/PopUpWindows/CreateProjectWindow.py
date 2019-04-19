from igor.Components.Core.PopUp import PopUpWindow
from PyQt5.QtWidgets import QFrame, QLineEdit, QVBoxLayout


class CreateProjectWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self, 'Load Project')
        self.frame = CreateProjectFrame(self)
        self.show()


class CreateProjectFrame(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.path = QLineEdit()
        self.layout.addWidget(self.path)
