from PyQt5.QtWidgets import QFrame, QHBoxLayout
from igor.Components.TestFrame.GridEditor import StepsContainer


class TestPanel(QFrame):

    def __init__(self, test_data):
        """

        :param test_data:
         :type test_data: TestCase
        """
        self.test_data = test_data
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        step_container = StepsContainer(test_data, self)
        self.layout.addWidget(step_container)
