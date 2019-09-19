import sys

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

class EncodeFile(QtWidgets.QWidget):
#class EncodeFile(QtWidgets.QObject):
    show_Result = QtCore.pyqtSignal(object)
    
    def __init__(self, imageData, config, CarrierDir, payloadDir): # payloadDir is payload directory
        super (EncodeFile, self).__init__()
        uic.loadUi('EncodeFile.ui', self)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        pixmap = QtGui.QPixmap()
        payloaddata = FileService.openFileContent(payloadDir)
        pixmap.loadFromData(payloaddata)
        self.label_2.setPixmap(pixmap)
        self.label_2.resize(pixmap.width(), pixmap.height())
        #self.lablabel_2el.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.setText("Next")
        self.pushButton_2.clicked.connect(self.ShowResult)


    def ShowResult(self):
        carrierWithPayload = re.sub(r'\.png', 'STEGGED.png', self.carrierDir)
        stegCommand = "python ./UIFiles/stegScript.py -e -f " + self.carrierDir
        + " " + self.payloadDir + " " + carrierWithPayload
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        ##stegResultImage =              ####### Your stegged image result should go here 
        #show_Result.emit(stegResultImage)
        show_Result.emit(carrierWithPayload)
