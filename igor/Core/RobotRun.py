from PyQt5.QtCore import QThread, pyqtSignal
from robot.run import run


class RobotRun(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, test_data, ):
        QThread.__init__(self)
        self.test_data = test_data

    def run(self):
        run(self.test_data)


class RunnerListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, signal):
        self.stream = signal
        pass

    def start_test(self, data, result):
        pass

    def end_test(self, data, result):
        pass

    def log_message(self, message):
        pass

    def message(self, message):
        pass
