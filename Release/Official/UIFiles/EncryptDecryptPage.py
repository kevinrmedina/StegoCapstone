import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from fileservice import FileService
import os
import subprocess
import re
from UIFiles import AesManager, DesManager, RsaManager


class EncryptDecryptPage(QtWidgets.QDialog):

    def __init__(self):
        super (EncryptDecryptPage, self).__init__()
        uic.loadUi('./UIFiles/encrypt_decrypt_pane.ui', self)
        self.input_file_path = ''
        self.output_file_path = ''
        self.public_key_path = ''
        self.private_key_path = ''
        self.algo_combobox = self.findChild(QtWidgets.QComboBox, 'algoCombobox')
        self.algo_combobox.addItems(['AES', 'DES', 'RSA'])
        self.encrypt_radio_button = self.findChild(QtWidgets.QRadioButton, 'encryptRadioButton')
        self.decrypt_radio_button = self.findChild(QtWidgets.QRadioButton, 'decryptRadioButton')
        self.input_file_button = self.findChild(QtWidgets.QPushButton, 'inputPushButton')
        self.output_file_button = self.findChild(QtWidgets.QPushButton, 'outputPushButton')
        self.input_file_path_line_edit = self.findChild(QtWidgets.QLineEdit, 'inputFilePath')
        self.output_file_path_line_edit = self.findChild(QtWidgets.QLineEdit, 'outputFilePath')
        self.input_file_path_line_edit.setReadOnly(True)
        self.output_file_path_line_edit.setReadOnly(True)
        self.password_label = self.findChild(QtWidgets.QLabel, 'passwordLabel')
        self.password_line_edit = self.findChild(QtWidgets.QLineEdit, 'passwordEdit')
        self.public_key_browse_button = self.findChild(QtWidgets.QPushButton, 'publicKeyButton')
        self.public_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'publicKeyFilePath')
        self.private_key_line_edit = self.findChild(QtWidgets.QLineEdit, 'privateKeyFilePath')
        self.private_key_browse_button = self.findChild(QtWidgets.QPushButton, 'privateKeyButton')
        self.finish_button = self.findChild(QtWidgets.QPushButton, 'finishButton')
        self.algo_combobox.currentIndexChanged.connect(self.__on_combobox_change)
        self.encrypt_radio_button.toggled.connect(self.__on_encrypt_radio_button_toggle)
        self.decrypt_radio_button.toggled.connect(self.__on_decrypt_radio_button_toggle)
        self.input_file_button.clicked.connect(self.__on_input_button_clicked)
        self.output_file_button.clicked.connect(self.__save_output)
        self.public_key_browse_button.clicked.connect(self.__on_pk_button_clicked)
        self.private_key_browse_button.clicked.connect(self.__on_pvk_button_clicked)
        self.finish_button.clicked.connect(self.__on_finish_button_clicked)

    def __on_combobox_change(self):
        index = self.algo_combobox.currentIndex()
        if index == 2:
            if self.encrypt_radio_button.isChecked():
                self.public_key_browse_button.setEnabled(True)
                self.private_key_browse_button.setEnabled(False)
                self.password_line_edit.setEnabled(False)
                self.password_label.setEnabled(False)

            else:
                self.private_key_browse_button.setEnabled(True)
                self.public_key_browse_button.setEnabled(False)
                self.password_line_edit.setEnabled(True)
                self.password_label.setEnabled(True)
        else:
            return

    def __on_encrypt_radio_button_toggle(self):
        if self.algo_combobox.currentIndex() == 2:
            self.public_key_browse_button.setEnabled(True)
            self.private_key_browse_button.setEnabled(False)
            self.password_line_edit.setEnabled(False)
            self.password_label.setEnabled(False)

    def __on_decrypt_radio_button_toggle(self):
        if self.algo_combobox.currentIndex() == 2:
            self.private_key_browse_button.setEnabled(True)
            self.public_key_browse_button.setEnabled(False)
            self.password_line_edit.setEnabled(True)
            self.password_label.setEnabled(True)

    def __on_input_button_clicked(self):
        self.input_file_path = FileService.openAnyFileNameDialog(self, self)
        self.input_file_path_line_edit.setText(self.input_file_path)

    def __save_output(self):
        file_path = FileService.saveFileDialog(self, self)
        self.output_file_path = file_path
        if file_path is not None and file_path != "":
            # file = open(file_path, 'wb')
            # file.close()
            self.output_file_path_line_edit.setText(file_path)
        else:
            #handle no file warning
            return None

    def __on_pk_button_clicked(self):
        self.public_key_path = FileService.openAnyFileNameDialog(self, self)
        self.public_key_line_edit.setText(self.public_key_path)

    def __on_pvk_button_clicked(self):
        self.private_key_path = FileService.openAnyFileNameDialog(self, self)
        self.private_key_line_edit.setText(self.public_key_path)

    def __on_finish_button_clicked(self):
        index = self.algo_combobox.currentIndex()
        if index == 0:
            if self.encrypt_radio_button.isChecked():
                password = self.password_line_edit.text()
                AesManager.write_encrypted_text(password, self.output_file_path, self.input_file_path)
            else:
                password = self.password_line_edit.text()
                AesManager.write_decrypted_text(password, self.output_file_path, self.input_file_path)
        elif index == 1:
            if self.encrypt_radio_button.isChecked():
                password = self.password_line_edit.text()
                DesManager.write_encrypted_text(password, self.output_file_path, self.input_file_path)
            else:
                password = self.password_line_edit.text()
                DesManager.write_decrypted_text(password, self.output_file_path, self.input_file_path)
        elif index == 2:
            if self.encrypt_radio_button.isChecked():
                public_key_file = open(self.public_key_path, 'rb')
                public_key = public_key_file.read()
                public_key_file.close()
                RsaManager.write_encrypted_stream(public_key, self.output_file_path, self.input_file_path)
            else:
                password = self.password_line_edit.text()
                private_key_file = open(self.private_key_path, 'rb')
                private_key = private_key_file.read()
                private_key_file.close()
                RsaManager.write_decrypted_stream(password, private_key, self.output_file_path, self.input_file_path)
        self.close()
