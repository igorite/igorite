from PyQt5.QtGui import QIcon
from os import path


class Images:

    PATH = path.abspath(path.dirname(__file__))
    CLOSE_ICON = None
    FOLDER_ICON = None
    KEYWORD_ICON = None
    KEYWORD_HIDE_ICON = None
    PLAY_ICON = None
    PYTHON_ICON = None
    TEST_ICON = None
    TEST_HIDE_ICON = None
    VARIABLE_ICON = None
    VARIABLE_HIDE_ICON = None
    APP_ICON = None
    TEST_CASE_FILE_ICON = None
    DELETE_ICON = None
    LIBRARIES_ICON = None
    RENAME_ICON = None
    SIMPLE_ARROW_UP_ICON = None
    SIMPLE_ARROW_DOWN_ICON = None

    def __init__(self):
        Images.TEST_CASE_FILE_ICON = QIcon(path.join(Images.PATH, 'test_case_file_icon.png'))
        Images.CLOSE_ICON = QIcon(path.join(Images.PATH, 'close.png'))
        Images.FOLDER_ICON = QIcon(path.join(Images.PATH, 'folder_icon.png'))
        Images.KEYWORD_ICON = QIcon(path.join(Images.PATH, 'keyword_icon.png'))
        Images.KEYWORD_HIDE_ICON = QIcon(path.join(Images.PATH, 'keyword_hide_icon.png'))
        Images.PLAY_ICON = QIcon(path.join(Images.PATH, 'play_icon.png'))
        Images.PYTHON_ICON = QIcon(path.join(Images.PATH, 'python_icon.png'))
        Images.TEST_ICON = QIcon(path.join(Images.PATH, 'test_icon.png'))
        Images.TEST_HIDE_ICON = QIcon(path.join(Images.PATH, 'test_hide_icon.png'))
        Images.VARIABLE_ICON = QIcon(path.join(Images.PATH, 'variable_icon.png'))
        Images.VARIABLE_HIDE_ICON = QIcon(path.join(Images.PATH, 'variable_hide_icon.png'))
        Images.APP_ICON = QIcon(path.join(Images.PATH, 'application_icon.png'))
        Images.DELETE_ICON = QIcon(path.join(Images.PATH, 'delete_icon.png'))
        Images.LIBRARIES_ICON = QIcon(path.join(Images.PATH, 'libraries_icon.png'))
        Images.RENAME_ICON = QIcon(path.join(Images.PATH, 'rename_icon.png'))
        Images.SIMPLE_ARROW_UP_ICON = QIcon(path.join(Images.PATH, 'simple_arrow_up_icon.png'))
        Images.SIMPLE_ARROW_DOWN_ICON = QIcon(path.join(Images.PATH, 'simple_arrow_down_icon.png'))
