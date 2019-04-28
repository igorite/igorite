from PyQt5.QtCore import QThread, pyqtSignal
from robot.run import run


class RobotRun(QThread):
    signal = pyqtSignal(list)

    def __init__(self, test_data):
        QThread.__init__(self)
        self.test_data = test_data

    def run(self):
        run(self.test_data, listener=RunnerListener(self.signal))


class RunnerListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, signal):
        self.stream = signal

    def start_suite(self, name, attributes):
        self.stream.emit(['start_suite', name, attributes])

    def end_suite(self, name, attributes):
        self.stream.emit(['end_test', name, attributes])

    def start_test(self, name, attributes):
        self.stream.emit(['start_test', name, attributes])

    def end_test(self, name, attributes):
        self.stream.emit(['end_test', name, attributes])

    def start_keyword(self, name, attributes):
        self.stream.emit(['start_keyword', name, attributes])

    def end_keyword(self, name, attributes):
        self.stream.emit(['end_keyword', name, attributes])

    def log_message(self, message):
        self.stream.emit(['log_message', message])

    def message(self, message):
        self.stream.emit(['message', message])

    def library_import(self, name, attributes):
        self.stream.emit(['library_import', name, attributes])

    def resource_import(self, name, attributes):
        self.stream.emit(['resource_import', name, attributes])
        pass

    def variable_import(self, name, attributes):
        self.stream.emit(['variable_import', name, attributes])
        pass

    def output_file(self, path):
        self.stream.emit(['output_file', path])

    def log_file(self, path):
        self.stream.emit(['log_file', path])

    def report_file(self, path):
        self.stream.emit(['report_file', path])

    def xunit_file(self, path):
        self.stream.emit(['xunit_file', path])

    def debug_file(self, path):
        self.stream.emit(['debug_file', path])

    def close(self):
        self.stream.emit(['close'])
