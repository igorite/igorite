from PyQt5.QtWidgets import QFrame, QVBoxLayout, QTableWidget, QTableWidgetItem


class StepsContainer(QFrame):

    def __init__(self, test_case, parent):
        """

        :param test_case:
        :type test_case: TestCase
        """
        QFrame.__init__(self)
        self.parent = parent
        self.test_case = test_case
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.steps_table = QTableWidget()
        self.steps_table.alternatingRowColors()
        self.steps_table.setRowCount(5)
        self.steps_table.setColumnCount(20)
        self.steps_table.setMinimumSize(80, 800)
        self.layout.addWidget(self.steps_table)
        self.add_steps()

    def add_steps(self):
        i = 0
        for step in self.test_case.steps:
            sed = QTableWidgetItem()
            sed.setText(step.name)
            self.steps_table.setItem(i, 0, sed)
            i += 1
