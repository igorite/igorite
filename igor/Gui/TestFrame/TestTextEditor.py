from PyQt5.Qsci import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFrame, QHBoxLayout
import re


class TestTextEditor(QFrame):

    def __init__(self, test_data):
        QFrame.__init__(self)
        print(test_data.parent.source)
        self.editor = QsciScintilla()
        self.editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(0, '0000')
        self.editor.setMarginsBackgroundColor(QColor(20, 20, 20))
        self.editor.setMarginsForegroundColor(QColor(230, 230, 230))
        self.lexer = RobotFrameworkLexer(self.editor)
        self.editor.setLexer(self.lexer)
        self.editor.setUtf8(True)

        with open(test_data.parent.source) as f:
            file = f.read()
            self.editor.append(str(file))

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.editor)
        self.setLayout(self.layout)
        self.lexer.styleText(0, self.editor.length())


class RobotFrameworkLexer(QsciLexerCustom):

    def __init__(self, parent):
        QsciLexerCustom.__init__(self, parent)
        self.parent = parent

        # Default values
        # ----------------------
        self.default_bg_color = QColor("#ff202020")
        self.font = QFont("Consolas", 12, weight=QFont.Bold)
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(self.default_bg_color)
        self.setDefaultFont(QFont("Consolas", 14))
        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#ffdddddd"), 0)  # Style 0: white
        self.setColor(QColor("#ff005500"), 1)  # Style 1: red
        self.setColor(QColor("#ff0000bf"), 2)  # Style 2: blue

        # Initialize paper colors per style
        # ----------------------------------
        self.setPaper(self.default_bg_color, 0)  # Style 0: default
        self.setPaper(self.default_bg_color, 1)  # Style 1: default
        self.setPaper(self.default_bg_color, 2)  # Style 2: default

        # Initialize fonts per style
        # ---------------------------
        self.setFont(self.font, 0)  # Style 0: 14pt bold
        self.setFont(self.font, 1)  # Style 1: 14pt bold
        self.setFont(self.font, 2)  # Style 2: 14pt bold

    @property
    def language(self):
        """
        This function return the language of the lexer

        :return: Lexer language
        :rtype: str
        """
        return 'Robot Framework'

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        elif style == 2:
            return "myStyle_2"
            ###
        return ""

    def styleText(self, start, end):
        # 1. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)

        # 2. Slice out a part from the text
        # ----------------------------------
        text = self.parent.text()[start:end]
        # 3. Tokenize the text
        # ---------------------
        p = re.compile(r"")
        token_list = [(token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]
        # -> 'token_list' is a list of tuples: (token_name, token_len)

        # 4. Style the text in a loop
        # ----------------------------
        # self.setStyling(number_of_chars, style_nr)
        #
        for i, token in enumerate(token_list):
            if token[0] in ["*** Settings ***",
                            "*** Test Cases ***",
                            "*** Keywords ***",
                            "*** Variables ***"]:
                # Title Style
                self.setStyling(token[1], 1)

            elif token[0] in ["[Template]"]:
                self.setStyling(token[1], 2)
            else:
                # Default style
                self.setStyling(token[1], 0)
            ###
        ###
