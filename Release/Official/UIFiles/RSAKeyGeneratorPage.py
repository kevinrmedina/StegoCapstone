import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from fileservice import FileService
from UIFiles.RsaKeyGeneration import RsaKeyGenerator


class RSAKeyGeneratorPage(QtWidgets.QDialog):

    def __init__(self):
        super(RSAKeyGeneratorPage, self).__init__()
        uic.loadUi('./UIFiles/generate_rsa_keys.ui', self)
        self.file_name_pub_key = None
        self.file_name_priv_key = None
        self.public_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'publicKeyFilePath')
        self.private_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'privateKeyFilePath')
        self.public_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.private_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.password_line_edit = self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit')
        self.generate_push_button = self.findChild(QtWidgets.QPushButton, 'generatePushbutton')
        self.public_key_line_edit.setReadOnly(True)
        self.private_key_line_edit.setReadOnly(True)
        self.public_key_file_path_button.clicked.connect(self.save_public)
        self.private_key_file_path_button.clicked.connect(self.save_private)
        self.generate_push_button.clicked.connect(self.generate_keys)

    def save_public(self):
        file_path = FileService.saveFileDialog(self, self)
        self.file_name_pub_key = file_path
        if file_path is not None and file_path != "":
            # file = open(file_path, 'wb')
            # file.close()
            self.public_key_line_edit.setText(file_path)
        else:
            #handle no file warning
            return None

    def save_private(self):
        file_path = FileService.saveFileDialog(self, self)
        self.file_name_priv_key = file_path
        if file_path is not None and file_path != "":
            # file = open(file_path, 'wb')
            # file.close()
            self.private_key_line_edit.setText(file_path)
        else:
            #handle no file warning
            return None

    def generate_keys(self):
        generator = RsaKeyGenerator()
        public_key = generator.generate_public_key()
        password = self.password_line_edit.text()
        private_key = generator.generate_private_key(password)
        public_key_file = open(self.file_name_pub_key, 'wb')
        public_key_file.write(public_key)
        public_key_file.close()
        private_key_file = open(self.file_name_priv_key, 'wb')
        private_key_file.write(private_key)
        private_key_file.close()
        self.close()



