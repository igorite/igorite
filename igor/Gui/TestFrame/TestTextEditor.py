from PyQt5.Qsci import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFrame, QHBoxLayout


class TestTextEditor(QFrame):

    def __init__(self):
        QFrame.__init__(self)

        self.editor = QsciScintilla()
        self.editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(0, '0000')
        self.editor.setMarginsBackgroundColor(QColor(20, 20, 20))
        self.editor.setMarginsForegroundColor(QColor(230, 230, 230))
        self.lexer = QsciLexerPython()
        self.lexer.setDefaultColor(QColor(0, 0, 20))
        self.lexer.setColor(QColor(30, 30, 30), 1)
        self.lexer.setDefaultPaper(QColor("#ffffffff"))
        self.lexer.setDefaultFont(QFont("Consolas", 14))
        self.editor.setLexer(self.lexer)
        self.editor.setUtf8(True)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.editor)
        self.setLayout(self.layout)