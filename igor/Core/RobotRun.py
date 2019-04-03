from PyQt5.QtCore import QThread, pyqtSignal
from robot.run import run


class RobotRun(QThread):
    signal = pyqtSignal(str)

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
        pass

    def end_suite(self, name, attributes):
        pass

    def start_test(self, name, attributes):
        self.stream.emit(str(attributes['starttime']) + ' ::INFO:: ' + str(attributes['longname']))

    def end_test(self, name, attributes):
        pass

    def start_keyword(self, name, attributes):
        self.stream.emit(str(attributes['starttime']) + ' ::INFO:: ' + str(attributes['kwname']))

    def end_keyword(self, name, attributes):
        pass

    def log_message(self, message):
        pass

    def message(self, message):
        pass

    def library_import(self, name, attributes):
        pass

    def resource_import(self, name, attributes):
        pass

    def variable_import(self, name, attributes):
        pass

    def output_file(self, path):
        pass

    def log_file(self, path):
        pass

    def report_file(self, path):
        pass

    def xunit_file(self, path):
        pass

    def debug_file(self, path):
        pass

    def close(self):
        pass
