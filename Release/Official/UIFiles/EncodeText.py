import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

class EncodeText(QtWidgets.QWidget):

    show_Result = QtCore.pyqtSignal(object, object, object, object, object)
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def ShowResult(self):
        self.EncodingString = self.decodeTextArea.toPlainText()
        print(self.EncodingString)
        newDir = re.sub(r'\.png', 'STEGGED.png', self.carrierDir)
        #stegCommand = "python ./UIFiles/stegScript.py -e -t " + " " + self.carrierDir + " " + newDir + " " + self.EncodingString
        stegCommand = "python ./UIFiles/stegScript.py -e -t " + " " + self.carrierDir + " " + newDir + " "
        stegCommand = stegCommand.split() + [self.EncodingString]
        subprocess.Popen(stegCommand)
        ENCODEDIMAGERESULT = newDir                    ####################### Encoded image result goes here, use self.EncodingString
        self.show_Result.emit(newDir, self.imageData, self.carrierDir, self.config, 3)
        
    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.carrierDir, 3)

    def __init__(self, imageData, config, CarrierDir):
        super (EncodeText, self).__init__()
        uic.loadUi('./UIFiles/EncodeText.ui', self)
        self.imageData = imageData
        self.config = config
        self.carrierDir = CarrierDir
        self.carrierLabel = self.findChild(QtWidgets.QLabel, 'carrierLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.carrierLabel.setPixmap(pixmap)
        self.carrierLabel.resize(pixmap.width(), pixmap.height())
        self.carrierLabel.setAlignment(QtCore.Qt.AlignCenter)  # center image carrierLabel
        self.decodeTextArea = self.findChild(QtWidgets.QTextEdit, 'encodeTextArea')
        self.EncodingString = self.decodeTextArea.toPlainText()         ######### STRING thats going to be encoded ################
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        # self.pushButton.setText("Next")
        self.pushButton.clicked.connect(self.ShowPrevious)
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'nextButton')
        # self.pushButton_2.setText("Next")
        self.pushButton_2.clicked.connect(self.ShowResult)
