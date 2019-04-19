from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout
from igor.Components.Core.PopUp import PopUpWindow
from igor.Gui.StyleSheet import style_sheet


class RunOptionsWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self,'Hola')
        self.layout = QHBoxLayout()
        self.layout.addWidget(RunOptionsWindowPanel())
        self.setStyleSheet(style_sheet)
        self.setLayout(self.layout)
        self.show()


class RunOptionsWindowPanel(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.label = QLabel('hola')
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)