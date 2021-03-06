from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re
import os.path
import time
from fileservice import FileService
import imghdr
from UIFiles import DesManager, AesManager, RsaManager

class DecodeFile(QtWidgets.QWidget):

    #show_Result = QtCore.pyqtSignal(object)
    gotoMainMenu = QtCore.pyqtSignal()
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def RestartDecode(self):
        self.gotoMainMenu.emit()
        pass

    def ShowPrevious(self):
        # Do what needs to be done
        self.switch_previous.emit(self.imageData, self.config, self.CarrierDir)
        pass

    def __init__(self, imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey):
        super (DecodeFile, self).__init__()
        uic.loadUi('./UIFiles/DecodeFile.ui', self)
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
        self.label_2 = self.findChild(QtWidgets.QLabel, 'payloadLabel_2')
        pixmap2 = QtGui.QPixmap()
        #newDir = "/home/kikohiho/Desktop/StegCapstone/StegoCapstone/Release/Official/UIFiles/recoveredFile" 
        newDir = re.sub(r'\/(?=[^/]*$).*', '/recoveredFile', self.CarrierDir)
        newDirCrypt = newDir + "Decrypted"
        stegCommand = "python ./UIFiles/stegScript.py -d -f " + self.CarrierDir + " " + newDir
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        while not os.path.exists(newDir):
            time.sleep(1)
        if self.cryptoAlgorithm == 1:  #AES
            AesManager.write_decrypted_text(self.password.encode('ascii'), newDirCrypt, newDir)
            if (imghdr.what(newDirCrypt) != None):
                payloaddata = FileService.openFileContent(self, newDirCrypt)                                ######### data of decoded image needs to go here 
                extension = os.path.splitext(newDirCrypt)
                pixmap2.loadFromData(payloaddata.read())
                self.label_2.setPixmap(pixmap2)
                self.label_2.resize(pixmap2.width(), pixmap2.height())
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
            else:
                self.label_2.setText(newDirCrypt)

        elif self.cryptoAlgorithm == 2:  #DES
            DesManager.write_decrypted_text(self.password.encode('ascii'), newDirCrypt, newDir)
            if (imghdr.what(newDirCrypt) != None):
                payloaddata = FileService.openFileContent(self, newDirCrypt)                                ######### data of decoded image needs to go here 
                extension = os.path.splitext(newDirCrypt)
                pixmap2.loadFromData(payloaddata.read())
                self.label_2.setPixmap(pixmap2)
                self.label_2.resize(pixmap2.width(), pixmap2.height())
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
            else:
                self.label_2.setText(newDirCrypt)

        elif self.cryptoAlgorithm == 3:  #RSA
            ####### THIS IS WHERE THE RSA PRIVATE KEY STUFF GOES MANUEL ############
            pvk_file = open(self.privateKey, 'rb')
            pvk_bytes = pvk_file.read()
            pvk_file.close()
            RsaManager.write_decrypted_stream(self.password.encode('ascii'), pvk_bytes, newDirCrypt, newDir)
            if imghdr.what(newDirCrypt) is not None:
                payloaddata = FileService.openFileContent(self, newDirCrypt)                                ######### data of decoded image needs to go here 
                extension = os.path.splitext(newDirCrypt)
                pixmap2.loadFromData(payloaddata.read())
                self.label_2.setPixmap(pixmap2)
                self.label_2.resize(pixmap2.width(), pixmap2.height())
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
            else:
                self.label_2.setText(newDirCrypt)

        elif self.cryptoAlgorithm == 0:  #Nothing
            if imghdr.what(newDir) is not None:
                payloaddata = FileService.openFileContent(self, newDir)                                ######### data of decoded image needs to go here 
                extension = os.path.splitext(newDir)
                pixmap2.loadFromData(payloaddata.read())
                self.label_2.setPixmap(pixmap2)
                self.label_2.resize(pixmap2.width(), pixmap2.height())
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
            else:
                self.label_2.setText(newDir)

        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.RestartDecode)
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        # self.pushButton.setText("Previous")
        self.pushButton.clicked.connect(self.ShowPrevious)

        
