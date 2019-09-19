
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import subprocess
import re

class DecodeFile(QtWidgets.QWidget):

    #show_Result = QtCore.pyqtSignal(object)

    def RestartDecode(self):
        # Do what needs to be done
        pass

    def __init__(self, imageData, config, CarrierDir):
        super (DecodeFile, self).__init__()
        uic.loadUi('./UIFiles/DecodeFile.ui', self)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        pixmap = QtGui.QPixmap()
        newDir = "recoveredFile" 
        stegCommand = "python ./UIFiles/stegScript.py -d -f " + self.CarrierDir + " " + newDir
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        payloaddata = newDir                                ######### data of decoded image needs to go here 
        pixmap.loadFromData(payloaddata)
        self.label_2.setPixmap(pixmap)
        self.label_2.resize(pixmap.width(), pixmap.height())
        self.lablabel_2el.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'pushButton_2')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.RestartDecode)

        
