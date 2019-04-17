from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLineEdit
from PyQt5.Qt import QFont


class StepsEditor(QFrame):

    def __init__(self, test_data):
        QFrame.__init__(self)
        self.test_data = test_data
        self.keywords_list = []

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        for step in self.test_data.steps:
            self.add_step(step.name)
        self.get_keywords()

    def add_step(self, keyword):
        self.layout.addWidget(Step(self, keyword))

    def get_keywords(self):
        test_keywords = self.test_data.parent.parent.keyword_table
        for keywords in test_keywords:
            self.keywords_list.append(keywords.name)

        print(self.keywords_list)


class Step(QFrame):

    def __init__(self, parent, main_keyword=None):
        QFrame.__init__(self)
        self.setMaximumSize(2000, 200)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.parent = parent

        font = QFont()
        font.setPointSize(16)

        self.main_keyword = QLineEdit()
        self.main_keyword.setFont(font)
        self.main_keyword.setText(main_keyword)
        self.layout.addWidget(self.main_keyword)

        self.tooltip = QFrame(self)
        self.tooltip.setGeometry(0, 0, 30, 30)
        self.tooltip.show()
        self.set_state()

    def set_state(self):
        if self.main_keyword.text() not in self.parent.keywords_list:
            self.main_keyword.setProperty('WRONG', True)
