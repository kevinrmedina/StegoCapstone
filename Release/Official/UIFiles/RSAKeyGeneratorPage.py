import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from Release.Official.fileservice import FileService

class RSAKeyGeneratorPage(QtWidgets.QDialog):

    def __init__(self):
        super(RSAKeyGeneratorPage, self).__init__()
        uic.loadUi('./UIFiles/generate_rsa_keys.ui', self)
        self.public_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'publicKeyFilePath')
        self.private_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'privateKeyFilePath')
        self.public_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.private_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.password_line_edit = self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit')
        self.generate_push_button = self.findChild(QtWidgets.QPushButton, 'generatePushButton')

    def save_file(self):
        file_path = FileService.saveFileDialog(self.Form, self.Form)
        if file_path is not None and file_path != "":
            file = FileService.write_file_content(self, file_path)
        else:
            #handle no file warning
            return None

