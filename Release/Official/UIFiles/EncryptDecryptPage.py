import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

class EncryptDecryptPage(QtWidgets.QDialog):

    def __init__(self):
        super (EncryptDecryptPage, self).__init__()
        uic.loadUi('./UIFiles/encrypt_decrypt_pane.ui', self)