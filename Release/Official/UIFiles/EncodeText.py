import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import time
import subprocess
import re
from UIFiles import AesManager, DesManager, RsaManager

class EncodeText(QtWidgets.QWidget):

    show_Result = QtCore.pyqtSignal(object, object, object, object, object)
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def ShowResult(self):
        self.EncodingString = self.decodeTextArea.toPlainText()
        newDir = re.sub(r'\.png', 'STEGGED.png', self.carrierDir)
        tempFilePT = '/tmp/tempFilePlainText'
        tempFileCT = "/tmp/tempFileCipherText"
        if self.cryptoAlgorithm == 1: #AES
            tempFilePlainText = open(tempFilePT, 'w')
            tempFilePlainText.write(self.EncodingString)
            tempFilePlainText.close()
            AesManager.write_encrypted_text(self.password.encode('ascii'), tempFileCT, tempFilePT)
            while os.path.isfile(tempFileCT) == False:
               time.wait(1)
            stegCommand = "python ./UIFiles/stegScript.py -e -f " + self.carrierDir + " " + tempFileCT + " " + newDir
            process = subprocess.Popen(stegCommand.split())
            process.wait()
            os.remove(tempFileCT)
            os.remove(tempFilePT)
            
        elif self.cryptoAlgorithm == 2: #DES
            tempFilePlainText = open(tempFilePT, 'w')
            tempFilePlainText.write(self.EncodingString)
            tempFilePlainText.close()
            DesManager.write_encrypted_text(self.password.encode('ascii'), tempFileCT, tempFilePT)
            while os.path.isfile(tempFileCT) == False:
               time.wait(1)
            stegCommand = "python ./UIFiles/stegScript.py -e -f " + " " + self.carrierDir + " " + tempFileCT + " " + newDir
            process = subprocess.Popen(stegCommand.split())
            process.wait()
            os.remove(tempFileCT)
            os.remove(tempFilePT)

        elif self.cryptoAlgorithm == 3: #RSA
            tempFilePlainText = open("tempFilePlainText", 'w')
            tempFilePlainText.write(self.EncodingString)
            tempFilePlainText.close()
            public_key_file_path = self.publicKey
            public_key_file = open(public_key_file_path, 'rb')
            public_key = public_key_file.read()
            public_key_file.close()
            RsaManager.write_encrypted_stream(public_key, tempFileCT, tempFilePT)
            while os.path.isfile(tempFileCT) == False:
               time.wait(1)
            stegCommand = "python ./UIFiles/stegScript.py -e -f " + " " + self.carrierDir + " " + tempFileCT + " " + newDir
            process = subprocess.Popen(stegCommand.split())
            process.wait()
            os.remove(tempFileCT)
            os.remove(tempFilePT)

        elif self.cryptoAlgorithm == 0: #Nothing
            stegCommand = "python ./UIFiles/stegScript.py -e -t " + " " + self.carrierDir + " " + newDir + " "
            stegCommand = stegCommand.split() + [self.EncodingString]
            subprocess.Popen(stegCommand)

        ENCODEDIMAGERESULT = newDir                    ####################### Encoded image result goes here, use self.EncodingString
        self.show_Result.emit(newDir, self.imageData, self.carrierDir, self.config, 3)
        
    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.carrierDir, 3)

    def __init__(self, imageData, config, CarrierDir, cryptoAlgorithm, password, publicKey):
        super (EncodeText, self).__init__()
        uic.loadUi('./UIFiles/EncodeText.ui', self)
        self.imageData = imageData
        self.config = config
        self.carrierDir = CarrierDir
        self.cryptoAlgorithm = cryptoAlgorithm
        self.password = password
        self.publicKey = publicKey
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
