import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

class RSAKeyGeneratorPage(QtWidgets.QDialog):

    def __init__(self):
        super(RSAKeyGeneratorPage, self).__init__()
        uic.loadUi('./UIFiles/generate_rsa_keys.ui', self)
        self.private_key_file_path_button = self.findChild(QtWidgets.QPushButton, 'privateKeyFilePath')