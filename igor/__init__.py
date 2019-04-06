import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication


from igor.Gui.main import MainWindow

if __name__ == '__main__':
    window = QApplication([])
    path = os.path.abspath(os.path.dirname(__file__))
    print(path)
    window.setWindowIcon(QIcon(os.path.join(path, 'Gui', 'images', 'IgorIcon.png')))
    app = MainWindow()
    sys.exit(window.exec_())
