import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from subprocess import check_output


class DecodeText(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (DecodeText, self).__init__()
        uic.loadUi('./UIFiles/DecodeText.ui', self)
        self.label = self.findChild(QtWidgets.QLabel, 'carrierImageLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.decodeTextArea = self.findChild(QtWidgets.QTextEdit, 'decodeTextArea')
        newDir = "recoveredFile"
        self.CarrierDir = CarrierDir
        stegCommand = "python ./UIFiles/stegScript.py -d -t " + self.CarrierDir
        # DECODEDTEXT = subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)                                            ######### Decoded text goes here ################
        DECODEDTEXT = check_output(stegCommand.split())
        print(DECODEDTEXT)
        self.decodeTextArea.setPlainText(DECODEDTEXT)
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'pushButton_2')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.RestartDecode)
