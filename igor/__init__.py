import os
import sys
import ctypes
from ctypes import wintypes

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication


from igor.Gui.main import MainWindow

if __name__ == '__main__':

    lpBuffer = wintypes.LPWSTR()
    AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
    AppUserModelID(ctypes.cast(ctypes.byref(lpBuffer), wintypes.LPWSTR))
    appid = lpBuffer.value
    ctypes.windll.kernel32.LocalFree(lpBuffer)
    if appid is not None:
        print(appid)
    window = QApplication([])
    app = MainWindow()
    sys.exit(window.exec_())
