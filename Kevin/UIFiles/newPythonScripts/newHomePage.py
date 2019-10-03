# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 478)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(18, 20, 631, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stegSleuthButton = QtWidgets.QPushButton(Form)
        self.stegSleuthButton.setGeometry(QtCore.QRect(40, 70, 131, 61))
        self.stegSleuthButton.setObjectName("stegSleuthButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Available Applications "))
        self.stegSleuthButton.setText(_translate("Form", "StegSleuth"))

