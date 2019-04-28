from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPlainTextEdit
from igor.Components.ReportViewer.ReportViewer import ReportViewer


class Runner(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.stream = QPlainTextEdit()
        self.stream.setObjectName('stream')
        # self.stream.setEnabled(False)
        self.layout.addWidget(self.stream)
        self.web = ReportViewer()
        self.text_separator = '========================================================================================'

    def add_text(self, log):

        if log[0] == 'start_test':
            self.start_test(log[1], log[2])

        if log[0] == 'end_test':
            self.end_test(log[1], log[2])

        if log[0] == 'log_message':
            self.log_message(log[1])

        if log[0] == 'start_keyword':
            self.start_keyword(log[1], log[2])

    def start_test(self, name, attributes):
        self.stream.appendPlainText(self.text_separator)
        self.stream.appendPlainText('TEST : ' + str(attributes['longname']))
        if attributes['tags']:
            self.stream.appendPlainText('TAGS:' + str(attributes['tags']))
        self.stream.appendPlainText('ID: ' + str(attributes['id']))
        if attributes['critical']:
            self.stream.appendPlainText('CRITICAL: ' + str(attributes['critical']))
        self.stream.appendPlainText('START TIME: ' + str(attributes['starttime']))
        if attributes['doc']:
            self.stream.appendPlainText('DOCUMENTATION: ' + str(attributes['doc']))
        self.stream.appendPlainText(self.text_separator)

    def end_test(self, name, attributes):
        self.stream.appendPlainText(self.text_separator)
        self.stream.appendPlainText('TEST : ' + str(attributes['longname']))
        self.stream.appendPlainText('ID: ' + str(attributes['id']))
        self.stream.appendPlainText(self.text_separator)

    def log_message(self, message):
        self.stream.appendPlainText(str(message['timestamp']
                                        + '  :: ' + message['level'] + ' :: '
                                        + str(message['message'])))

    def start_keyword(self, name, attributes):
        self.stream.appendPlainText(str(attributes['starttime'])
                                        + '  :: ' + 'INFO' + ' :: '
                                        + str(attributes['kwname']))
