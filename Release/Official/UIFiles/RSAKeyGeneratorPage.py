import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from fileservice import FileService


class RSAKeyGeneratorPage(QtWidgets.QDialog):

    def __init__(self):
        super(RSAKeyGeneratorPage, self).__init__()
        uic.loadUi('./UIFiles/generate_rsa_keys.ui', self)
        self.file_name = None
        self.public_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'publicKeyFilePath')
        self.private_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'privateKeyFilePath')
        self.public_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.private_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.password_line_edit = self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit')
        self.generate_push_button = self.findChild(QtWidgets.QPushButton, 'generatePushButton')
        self.public_key_line_edit.setReadOnly(True)
        self.private_key_line_edit.setReadOnly(True)
        self.public_key_file_path_button.clicked.connect(self.save_public)
        self.private_key_file_path_button.clicked.connect(self.save_private)

    def save_public(self):
        file_path = FileService.saveFileDialog(self, self)
        self.file_name = file_path
        if file_path is not None and file_path != "":
            file = open(file_path, 'wb')
            file.close()
            self.public_key_line_edit.setText(file_path)
        else:
            #handle no file warning
            return None

    def save_private(self):
        file_path = FileService.saveFileDialog(self, self)
        self.file_name = file_path
        if file_path is not None and file_path != "":
            file = open(file_path, 'wb')
            file.close()
            self.private_key_line_edit.setText(file_path)
        else:
            #handle no file warning
            return None

