# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/EncryptionGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EncryptionPage(QtCore.QObject):
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
        self.switch_window.emit(self.imagedata, self.Config, self.carrierDir)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(639, 550)
        Form.setFixedSize(750, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.algorithmComboBox = QtWidgets.QComboBox(Form)
        self.algorithmComboBox.setObjectName("algorithmComboBox")
        self.algorithmComboBox.addItem("")
        self.algorithmComboBox.addItem("")
        self.algorithmComboBox.addItem("")
        self.verticalLayout.addWidget(self.algorithmComboBox)
        self.keyLabel = QtWidgets.QLabel(Form)
        self.keyLabel.setObjectName("keyLabel")
        self.verticalLayout.addWidget(self.keyLabel)
        self.keyTextEdit = QtWidgets.QTextEdit(Form)
        self.keyTextEdit.setObjectName("keyTextEdit")
        self.verticalLayout.addWidget(self.keyTextEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.previousPushButton = QtWidgets.QPushButton(Form)
        self.previousPushButton.setObjectName("previousPushButton")
        self.horizontalLayout_4.addWidget(self.previousPushButton)
        self.nextPushButton = QtWidgets.QPushButton(Form)
        self.nextPushButton.setEnabled(True)
        self.nextPushButton.setObjectName("nextPushButton")
        self.nextPushButton.clicked.connect(self.EmitSwitch)
        self.horizontalLayout_4.addWidget(self.nextPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Encrypt"))
        self.label.setText(_translate("Form", "Encryption Algorithm:"))
        self.algorithmComboBox.setItemText(0, _translate("Form", "AES"))
        self.algorithmComboBox.setItemText(1, _translate("Form", "DES"))
        self.algorithmComboBox.setItemText(2, _translate("Form", "RSA"))
        self.keyLabel.setText(_translate("Form", "Key:"))
        self.previousPushButton.setText(_translate("Form", "Previous"))
        self.nextPushButton.setText(_translate("Form", "Next"))
