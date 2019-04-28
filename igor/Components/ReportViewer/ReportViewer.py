
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView



class ReportViewer(QFrame):

    def __init__(self, ):
        QFrame.__init__(self)

        self.web = QWebEngineView()
        path = QUrl.fromLocalFile('C:\\Users\\3l1n\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\igorite\igor\\report.html')
        self.web.load(path)
        self.web.show()