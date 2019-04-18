from igor.Gui.PopUpWindows.PopUp import PopUpWindow
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QTableWidget, QTableWidgetItem
import subprocess


class GitLogWindow(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self, 'Show Log')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(GitLogFrame())
        self.show()


class GitLogFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.log_table = QTableWidget()
        self.log_table.setColumnCount(4)
        self.log_table.setRowCount(40)

        self.layout.addWidget(self.log_table)
        self.get_git_log()

    def get_git_log(self):
        lines = (subprocess.check_output(['git', 'log', ], stderr=subprocess.STDOUT)
                 .decode("utf-8")
                 .split('\n'))
        row = 0
        commit = False
        author = False
        date = False

        lines = list(filter(None, lines))
        for i, line in enumerate(lines):
            print(line)
            item = QTableWidgetItem()
            item.setText(line)
            print('start '+str(line[0:6]))
            if line[0:6] == 'commit':
                print('hey')
                self.log_table.setItem(row, 0, item)
                commit = True
            elif line[0:6] == 'Author':
                self.log_table.setItem(row, 1, item)
                author = True
            elif line[0:4] == 'Date':
                self.log_table.setItem(row, 2, item)
                date = True
            elif commit and author and date:
                if line[0:6] != 'commit':
                    self.log_table.setItem(row, 3, item)
                    row += 1
                else:
                    row += 1
                    self.log_table.setItem(row, 0, item)
                    commit = True
