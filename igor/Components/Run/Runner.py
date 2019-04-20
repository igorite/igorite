from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPlainTextEdit


class Runner(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.stream = QPlainTextEdit()
        self.stream.setObjectName('stream')
        # self.stream.setEnabled(False)
        self.layout.addWidget(self.stream)

    def add_text(self, text):
        self.stream.appendPlainText(text)
