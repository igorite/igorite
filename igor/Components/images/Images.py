from PyQt5.QtGui import QIcon
from os import path


class Images:

    PATH = path.abspath(path.dirname(__file__))
    CLOSE_ICON = None
    FOLDER_ICON = None
    KEYWORD_ICON = None
    PLAY_ICON = None
    PYTHON_ICON = None
    TEST_ICON = None
    VARIABLE_ICON = None
    APP_ICON = None
    TEST_CASE_FILE_ICON = None

    def __init__(self):
        Images.TEST_CASE_FILE_ICON = QIcon(path.join(Images.PATH, 'test_case_file_icon.png'))
        Images.CLOSE_ICON = QIcon(path.join(Images.PATH, 'close.png'))
        Images.FOLDER_ICON = QIcon(path.join(Images.PATH, 'folder_icon.png'))
        Images.KEYWORD_ICON = QIcon(path.join(Images.PATH, 'keyword_icon.png'))
        Images.PLAY_ICON = QIcon(path.join(Images.PATH, 'play_icon.png'))
        Images.PYTHON_ICON = QIcon(path.join(Images.PATH, 'python_icon.png'))
        Images.TEST_ICON = QIcon(path.join(Images.PATH, 'test_icon.png'))
        Images.VARIABLE_ICON = QIcon(path.join(Images.PATH, 'variable_icon.png'))
        Images.APP_ICON = QIcon(path.join(Images.PATH, 'application_icon.png'))
