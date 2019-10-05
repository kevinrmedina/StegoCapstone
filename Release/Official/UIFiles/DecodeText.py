import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from subprocess import check_output


class DecodeText(QtWidgets.QWidget):

    gotoMainMenu = QtCore.pyqtSignal()
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def MainMenu(self):
        self.gotoMainMenu.emit()
        pass
    
    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.CarrierDir)
        pass

    def __init__(self, imageData, config, CarrierDir):
        super (DecodeText, self).__init__()
        uic.loadUi('./UIFiles/DecodeText.ui', self)
        self.imageData = imageData
        self.config = config
        self.CarrierDir = CarrierDir
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
        self.decodeTextArea.setPlainText(DECODEDTEXT.decode("utf-8"))
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.clicked.connect(self.MainMenu)
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        self.pushButton.clicked.connect(self.ShowPrevious)
