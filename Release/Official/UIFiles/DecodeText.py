import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
from UIFiles import AesManager, DesManager, RsaManager

class DecodeText(QtWidgets.QWidget):

    gotoMainMenu = QtCore.pyqtSignal()
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def MainMenu(self):
        self.gotoMainMenu.emit()
        pass
    
    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.CarrierDir)
        pass

    def __init__(self, imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey):
        super (DecodeText, self).__init__()
        uic.loadUi('./UIFiles/DecodeText.ui', self)
        self.imageData = imageData
        self.config = config
        self.CarrierDir = CarrierDir
        self.cryptoAlgorithm = cryptoAlgorithm
        self.password = password
        self.privateKey = privateKey
        self.label = self.findChild(QtWidgets.QLabel, 'carrierLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.decodeTextArea = self.findChild(QtWidgets.QTextEdit, 'decodeTextArea')
        #tempFileEncrypted = re.sub(r'\/(?=[^/]*$).*', '/tempFileEncrypted', self.CarrierDir) 
        #tempFileDecrypted = re.sub(r'\/(?=[^/]*$).*', '/tempFileDecrypted', self.CarrierDir) 
        tempFileEncrypted = '/tmp/tempFileEncrypted'
        tempFileDecrypted = '/tmp/tempFileDecrypted'
        stegCommandText = "python ./UIFiles/stegScript.py -d -t " + self.CarrierDir
        stegCommandFile = "python ./UIFiles/stegScript.py -d -f " + self.CarrierDir + ' ' + tempFileEncrypted
        if self.cryptoAlgorithm == 1: #AES
            process = subprocess.Popen(stegCommandFile.split())
            process.wait()
            AesManager.write_decrypted_text(self.password.encode('ascii'), tempFileDecrypted, tempFileEncrypted)
            fileWithText = open(tempFileDecrypted, 'r')
            extractedText = fileWithText.read()
            fileWithText.close()
            os.remove(tempFileEncrypted)
            os.remove(tempFileDecrypted)
            self.decodeTextArea.setPlainText(extractedText)
        
        elif self.cryptoAlgorithm == 2: #DES
            process = subprocess.Popen(stegCommandFile.split())
            process.wait()
            DesManager.write_decrypted_text(self.password.encode('ascii'), tempFileDecrypted, tempFileEncrypted)
            os.remove(tempFileEncrypted)
            fileWithText = open(tempFileDecrypted, 'r')
            extractedText = fileWithText.read()
            fileWithText.close()
            os.remove(tempFileDecrypted)
            self.decodeTextArea.setPlainText(extractedText)
        
        elif self.cryptoAlgorithm == 3: #RSA
            subprocess.Popen(stegCommandFile.split())
            pvk_file = open(self.privateKey, 'rb')
            pvk_bytes = pvk_file.read()
            pvk.close()
            RsaManager.write_decrypted_stream(self.password.encode('ascii'), pvk_bytes, tempFileDecrypted, tempFileEncrypted)
            os.remove(tempFileEncrypted)
            fileWithText = open(tempFileDecrypted, 'r')
            extractedText = fileWithText.read()
            fileWithText.close()
            os.remove(tempFileDecrypted)
            self.decodeTextArea.setPlainText(extractedText)

        elif self.cryptoAlgorithm == 0: #Nothing
            DECODEDTEXT = subprocess.check_output(stegCommandText.split())
            self.decodeTextArea.setPlainText(DECODEDTEXT.decode("utf-8"))
        
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.clicked.connect(self.MainMenu)
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        self.pushButton.clicked.connect(self.ShowPrevious)
