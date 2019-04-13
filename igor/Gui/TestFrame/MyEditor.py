from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QStandardItemModel, QStandardItem, QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QCompleter, QTextEdit
from os import path
from igor.Gui.StyleSheet import style_sheet


class TextEdit(QTextEdit):

    def __init__(self,test_data, parent=None):
        super(TextEdit, self).__init__(parent)
        self.test_data = test_data
        self.path = path.abspath(path.dirname(__file__))

        font_id = QFontDatabase.addApplicationFont(path.join(path.dirname(self.path),
                                                             'font',
                                                             'FiraCode-Medium.ttf'))
        print(font_id)
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(family)
        self.font = QFont()
        self.font.setPointSize(20)
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

    def get_keywords(self):
        for keyword in self.test_data.parent.parent.keyword_table:
            item = QStandardItem(keyword.name)
            print(keyword.name)
            item.setData(keyword.name)
            item.setIcon(self.keyword_icon)
            print(self.items.rowCount())
            self.items.setItem(self.items.rowCount(),item)


    def set_completer(self, c):
        if self._completer is not None:
            self._completer.activated.disconnect()

        self._completer = c

        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        c.activated.connect(self.insert_completion)

    def completer(self):
        return self._completer

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
        completion_prefix = self.text_under_cursor()

        if (not is_shortcut
            and (has_modifier
                 or len(e.text()) == 0
                 or len(completion_prefix) < 2
                 or e.text()[-1] in eow)):

            self._completer.popup().hide()
            return

        if completion_prefix != self._completer.completionPrefix():
            self._completer.setCompletionPrefix(completion_prefix)
            self._completer_popup = self._completer.popup()
            self._completer.popup().setCurrentIndex(
                    self._completer.completionModel().index(0, 0))

        cr = self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(0)
                    + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)
