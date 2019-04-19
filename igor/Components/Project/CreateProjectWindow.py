# Copyright 2019 Igorite
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ----------------------------------
# Imports
# ----------------------------------
from pathlib import Path
from igor.Components.Core.PopUp import PopUpWindow
from PyQt5.QtWidgets import QFrame, QLineEdit, QVBoxLayout, QGridLayout, QLabel, QPushButton, QFileDialog
import json
import os


class CreateProjectWindow(PopUpWindow):

    def __init__(self):
        # ----------------------------------
        # Initialize Window
        # ----------------------------------

        PopUpWindow.__init__(self, 'Create Project')
        # ----------------------------------
        # Create layout Manager
        # ----------------------------------

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # ----------------------------------
        # Add Git log Table to the frame
        # ----------------------------------

        self.layout.addWidget(CreateProjectFrame(self))
        self.show()
        self.adjustSize()  # Adjust the size of the window to fit the data
        self.setFixedSize(self.size())  # Do not allow resize the window


class CreateProjectFrame(QFrame):

    def __init__(self, parent=None):
        # ----------------------------------
        # Initialize Frame
        # ----------------------------------

        QFrame.__init__(self, parent=parent)
        self.window = parent
        self.file_dialog = None
        self.current_path = self.get_home_directory()
        self.project_data = {}
        # ----------------------------------
        # Create layout Manager
        # ----------------------------------

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        # ----------------------------------
        # Create form
        # ----------------------------------

        self.project_name_label = QLabel()
        self.project_name_label.setText('Project Name: ')
        self.layout.addWidget(self.project_name_label, 0, 0)
        # ----------------------------------

        self.project_name_text = QLineEdit()
        self.project_name_text.textChanged.connect(self.update_path_with_project_name)
        self.layout.addWidget(self.project_name_text, 0, 1)
        # ----------------------------------

        self.path_label = QLabel()
        self.path_label.setText('Path: ')
        self.layout.addWidget(self.path_label, 1, 0)
        # ----------------------------------

        self.path_text = QLineEdit()
        self.path_text.setText(self.current_path)
        self.layout.addWidget(self.path_text, 1, 1)
        # ----------------------------------

        self.path_browse_button = QPushButton()
        self.path_browse_button.setText('Browse...')
        self.path_browse_button.clicked.connect(self.directory_search)
        self.layout.addWidget(self.path_browse_button, 1, 2)
        # ----------------------------------
        self.create_project_button = QPushButton()
        self.create_project_button.setText('Create Project')
        self.create_project_button.clicked.connect(self.create_project)
        self.layout.addWidget(self.create_project_button, 2, 0)

    def directory_search(self):
        """
        This function create a File Dialog to select a directory path
        :return: None
        """
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        self.file_dialog.show()
        self.current_path = self.file_dialog.selectedFiles()[0]
        self.path_text.setText(self.current_path)

    @staticmethod
    def get_home_directory():
        """
        This function returns the home directory of the user
        :return (str): the home directory of the user
        """
        home_directory = str(Path.home())  # Get the home directory
        home_directory.replace('\\', '/')  # parse the home directory
        return home_directory

    def update_path_with_project_name(self, event):
        """
        This functions update the project path with the desired path plus the project name folder
        :return: None
        """
        self.path_text.setText(self.current_path + '\\' + self.project_name_text.text())

    def create_project(self):
        """
        This function creates project
        :return:
        """
        # ----------------------------------
        # get the project data
        # ----------------------------------

        project_name = self.project_name_text.text()
        path = self.path_text.text()
        # ----------------------------------
        # create the project data
        # ----------------------------------

        self.project_data['project_name'] = project_name
        self.project_data['project_path'] = path
        # ----------------------------------
        # Create the project directory if do not exist
        # ----------------------------------

        if not os.path.exists(path):
            os.mkdir(path)
        # ----------------------------------
        # create the project data file
        # ----------------------------------
        json_path = os.path.join(str(self.project_data['project_path']), '.igorite')

        # create the directory if do not exist
        if not os.path.exists(json_path):
            os.mkdir(json_path)

        # dump the project data to a json file
        with open(json_path + '\\data.igt', 'w') as outfile:
            json.dump(self.project_data, outfile)
        # ----------------------------------
        # Close the project creator window
        # ----------------------------------

        self.window.close()
