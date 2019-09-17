# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/TextPayloadPage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
#### ENCODE TEXT PAGE

from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import subprocess
import re

class TextPayloadPage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts
    def __init__(self, imageData, config, CarrierDir):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        self.imagedata = imageData
        self.carrierDir = CarrierDir
        self.Config = config
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self): # implement event that will emit the switch window signal 
        #Steg STUUUUUUUFFF
        carrierWithPayload = re.sub(r'\.png', 'STEGGED.png', self.carrierDir)
        stegCommand = "python ./UIFiles/stegScript.py -e -t " + self.carrierDir + " " + carrierWithPayload + " " + self.plainTextEdit.toPlainText() 
        subprocess.Popen(stegCommand.split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()
        #subprocess.Popen(["python", "./UIFiles/stegScript.py", "-h"])
        # steg = LSBSteg(plt.imread(self.carrierDir))
        # print("Image Read")
        # carrier_encoded = steg.encode_text(self.plainTextEdit.toPlainText())
        # print("Image encoded with text")
        # plt.imwrite(self.carrierDir + ".hid")
        # print ("Image Saved")
        # print(self.carrierDir)
        self.switch_window.emit(self.imagedata, self.Config, self.carrierDir)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(638, 496)
        Form.setFixedSize(750, 550)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(390, 400, 221, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.EmitSwitch)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 80, 221, 271))
        # self.label_2.setText("")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.imagedata)
        self.label_2.setPixmap(pixmap)
        self.label_2.resize(pixmap.width(), pixmap.height())
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 90, 251, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Prev"))
        self.pushButton_4.setText(_translate("Form", "Next"))
        self.plainTextEdit.setPlainText(_translate("Form", "Enter secret message here\n"""))
