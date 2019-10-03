# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowsePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 550)
        self.browseFileButton = QtWidgets.QPushButton(Form)
        self.browseFileButton.setGeometry(QtCore.QRect(305, 450, 131, 51))
        self.browseFileButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.browseFileButton.setObjectName("browseFileButton")
        self.logoLabel = QtWidgets.QLabel(Form)
        self.logoLabel.setGeometry(QtCore.QRect(140, 0, 471, 401))
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browseFileButton.setText(_translate("Form", "Browse File"))
        self.logoLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/Application Logo/Release/Official/StegSleuth1.png\"/></p></body></html>"))

#import Application Logo_rc
