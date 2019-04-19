# Copyright 2019 SocIsomer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import (QTextCursor, QStandardItemModel, QStandardItem, QIcon, QFont,
                         QFontDatabase, QSyntaxHighlighter, QTextCharFormat)
from PyQt5.QtWidgets import QCompleter, QTextEdit
from os import path
from igor.Gui.StyleSheet import style_sheet


class TextEdit(QTextEdit):

    def __init__(self, test_data, parent=None):
        super(TextEdit, self).__init__(parent)
        self.test_data = test_data
        self.path = path.abspath(path.dirname(__file__))
        with open(test_data.parent.source) as f:
            file = f.read()
            self.append(str(file))

        font_id = QFontDatabase.addApplicationFont(path.join(path.dirname(self.path),
                                                             'font',
                                                             'FiraCode-Medium.ttf'))
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.highlighter = RobotFrameworkHighlighter(self)
        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setFamily(family)
        self.setFont(self.font)
        self._completer = None
        self.keyword_icon = QIcon(path.join(self.path, '..', 'images', 'keyword_icon.png'))
        self.completer = QCompleter(self)
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setWrapAround(False)
        self.set_completer(self.completer)
        self.items = QStandardItemModel()
        self.get_keywords()
        self._completer_popup = self._completer.popup()
        self._completer_popup.setStyleSheet(style_sheet)
        self._completer_popup.setFont(self.font)
        self.completer.setModel(self.items)
        self.completion_prefix = ''

    def get_keywords(self):
        for keyword in self.test_data.parent.parent.keyword_table:
            item = QStandardItem(keyword.name)
            print(keyword.name)
            item.setData(keyword.name)
            item.setIcon(self.keyword_icon)
            print(self.items.rowCount())
            self.items.setItem(self.items.rowCount(), item)

    def set_completer(self, c):
        if self._completer is not None:
            self._completer.activated.disconnect()

        self._completer = c

        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        c.activated.connect(self.insert_completion)

    def insert_completion(self, completion):
        if self._completer.widget() is not self:
            return

        tc = self.textCursor()
        extra = len(completion) - len(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])

    def text_under_cursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        current_length = len(self.completion_prefix)
        if (self._completer.currentCompletion()[0:current_length].lower() == self.completion_prefix.lower()
                and self.completion_prefix != ''):

            if tc.selectedText() == '':
                print('hey')
                return self.completion_prefix + ' '
            else:
                return self.completion_prefix + tc.selectedText()[:-1]
        return tc.selectedText()

    def focusInEvent(self, e):

        if self._completer is not None:
            self._completer.setWidget(self)
        super(TextEdit, self).focusInEvent(e)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_E:
            self.insertPlainText('e')
        if self._completer is not None and self._completer.popup().isVisible():
            # The following keys are forwarded by the completer to the widget.
            if e.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                e.ignore()
                # Let the completer do default behavior.
                return

        is_shortcut = ((e.modifiers() & Qt.ControlModifier) != 0 and e.key() == Qt.Key_E)
        if self._completer is None or not is_shortcut:
            # Do not process the shortcut when we have a completer.
            super(TextEdit, self).keyPressEvent(e)

        ctrl_or_shift = e.modifiers() & (Qt.ControlModifier | Qt.ShiftModifier)
        if self._completer is None or (ctrl_or_shift and len(e.text()) == 0):
            return

        eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
        has_modifier = (e.modifiers() != Qt.NoModifier) and not ctrl_or_shift
        self.completion_prefix = self.text_under_cursor()

        if (not is_shortcut
                and (has_modifier
                     or len(e.text()) == 0
                     or len(self.completion_prefix) < 2
                     or e.text()[-1] in eow)):
            self._completer.popup().hide()
            return

        if self.completion_prefix != self._completer.completionPrefix():
            self._completer.setCompletionPrefix(self.completion_prefix)
            self._completer_popup = self._completer.popup()
            self._completer.popup().setCurrentIndex(
                self._completer.completionModel().index(0, 0))

        cr = self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(0)
                    + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)


class RobotFrameworkHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(RobotFrameworkHighlighter, self).__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)

        keyword_patterns = ["\\bGiven\\b", "\\bWhen\\b", "\\band\\b",
                            "\\bThen\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                            "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                            "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                            "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                            "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                            "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                            "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                            "\\bvolatile\\b"]

        self.highlightingRules = [(QRegExp(pattern), keyword_format)
                                  for pattern in keyword_patterns]

        class_format = QTextCharFormat()
        class_format.setFontWeight(QFont.Bold)
        class_format.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                                       class_format))

        single_line_comment_format = QTextCharFormat()
        single_line_comment_format.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("user types .*"),
                                       single_line_comment_format))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotation_format = QTextCharFormat()
        quotation_format.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotation_format))

        separators_format = QTextCharFormat()
        separators_format.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\*.*\*"), separators_format))

        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(Qt.darkYellow)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                                       function_format))

        documentation_format = QTextCharFormat()
        documentation_format.setForeground(Qt.green)
        self.highlightingRules.append((QRegExp("[.][.][.]"), documentation_format))
        self.highlightingRules.append((QRegExp("[.][.][.] .*"), documentation_format))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format_text in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format_text)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != 1:
            start_index = self.commentStartExpression.indexIn(text)

        while start_index >= 0:
            end_index = self.commentEndExpression.indexIn(text, start_index)

            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
            else:
                comment_length = end_index - start_index + self.commentEndExpression.matchedLength()

            self.setFormat(start_index, comment_length,
                           self.multiLineCommentFormat)
            start_index = self.commentStartExpression.indexIn(text,
                                                              start_index + comment_length)
