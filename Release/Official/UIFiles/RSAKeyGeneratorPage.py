# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_rsa_keys.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from fileservice import FileService

from UIFiles.RsaKeyGeneration import RsaKeyGenerator


class RSAKeyGeneratorPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.publicKeyFilePath = QtWidgets.QPushButton(Dialog)
        self.publicKeyFilePath.setObjectName("publicKeyFilePath")
        self.horizontalLayout_3.addWidget(self.publicKeyFilePath)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.privateKeyFilePath = QtWidgets.QPushButton(Dialog)
        self.privateKeyFilePath.setObjectName("privateKeyFilePath")
        self.horizontalLayout_2.addWidget(self.privateKeyFilePath)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.generatePushbutton = QtWidgets.QPushButton(Dialog)
        self.generatePushbutton.setObjectName("generatePushbutton")
        self.horizontalLayout_4.addWidget(self.generatePushbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate RSA Keys"))
        self.publicKeyFilePath.setText(_translate("Dialog", "Public Key Path"))
        self.privateKeyFilePath.setText(_translate("Dialog", "Private Key Path"))
        self.passwordLabel.setText(_translate("Dialog", "Private Key Password:"))
        self.generatePushbutton.setText(_translate("Dialog", "Generate"))


    def save_file(self):
        file_path = FileService.saveFileDialog(self.Form, self.Form)
        if file_path is not None and file_path != "":
            file = open(file_path, 'wb')
            file.close()
            return file_path
        else:
            # handle no file warning
            return None
