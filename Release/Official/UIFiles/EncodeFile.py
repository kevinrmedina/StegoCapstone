import sys

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import os.path
import subprocess
import re
from fileservice import FileService


class EncodeFile(QtWidgets.QWidget):
    show_Result = QtCore.pyqtSignal(object, object, object, object, object, object)
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.carrierDir)


    def __init__(self, imageData, config, CarrierDir, payloadDir): # payloadDir is payload directory
        super (EncodeFile, self).__init__()
        uic.loadUi('./UIFiles/EncodeFile.ui', self)
        self.setFixedSize(750, 550)
        self.payloadDir = payloadDir
        self.imageData = imageData
        self.config = config
        self.carrierDir = CarrierDir
        self.label = self.findChild(QtWidgets.QLabel, 'carrierLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        # self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'payloadLabel')
        pixmap = QtGui.QPixmap()
        #TODO Validate payload Dir
        extension = os.path.splitext(payloadDir)[1]
        print(extension)
        if (extension == ".png" or extension == ".jpeg" or extension == ".jpg" or extension == ".gif"):
            payloaddata = FileService.openFileContent(self, payloadDir)
            pixmap.loadFromData(payloaddata.read())
            self.label_2.setPixmap(pixmap)
            # self.label_2.resize(pixmap.width(), pixmap.height())
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image labelself.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        else:
            self.label_2.setText(payloadDir)
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'nextButton')
        # self.pushButton_2.setText("Next")
        self.pushButton_2.clicked.connect(self.ShowResult)
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        # self.pushButton_2.setText("Next")
        self.pushButton.clicked.connect(self.ShowPrevious)

    def ShowResult(self):
        carrierWithPayload = re.sub(r'\.png', 'STEGGED.png', self.carrierDir)
        stegCommand = "python ./UIFiles/stegScript.py -e -f " + self.carrierDir + " " + self.payloadDir + " " + carrierWithPayload
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        ##stegResultImage =              ####### Your stegged image result should go here 
        #show_Result.emit(stegResultImage)
        self.show_Result.emit(carrierWithPayload, self.imageData, self.carrierDir, self.config, 1, self.payloadDir)
