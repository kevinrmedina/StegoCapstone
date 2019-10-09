from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

from fileservice import FileService

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

    def __init__(self, imageData, config, CarrierDir):
        super (DecodeFile, self).__init__()
        uic.loadUi('./UIFiles/DecodeFile.ui', self)
        self.imageData = imageData
        self.config = config
        self.CarrierDir = CarrierDir
        self.label = self.findChild(QtWidgets.QLabel, 'carrierLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'payloadLabel_2')
        pixmap2 = QtGui.QPixmap()
        newDir = "recoveredFile" 
        stegCommand = "python ./UIFiles/stegScript.py -d -f " + self.CarrierDir + " " + newDir
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        payloaddata = FileService.openFileContent(self, newDir)                                ######### data of decoded image needs to go here 
        pixmap2.loadFromData(payloaddata.read())
        self.label_2.setPixmap(pixmap2)
        self.label_2.resize(pixmap2.width(), pixmap2.height())
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.RestartDecode)
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        # self.pushButton.setText("Previous")
        self.pushButton.clicked.connect(self.ShowPrevious)

        
