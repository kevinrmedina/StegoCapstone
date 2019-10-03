# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeText.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 550)
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setGeometry(QtCore.QRect(430, 450, 113, 51))
        self.previousButton.setObjectName("previousButton")
        self.encodeTextArea = QtWidgets.QTextEdit(Form)
        self.encodeTextArea.setGeometry(QtCore.QRect(10, 10, 359, 421))
        self.encodeTextArea.setObjectName("encodeTextArea")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(560, 450, 113, 51))
        self.nextButton.setObjectName("nextButton")
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(380, 10, 362, 421))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.carrierLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carrierLabel.setObjectName("carrierLabel")
        self.gridLayout_3.addWidget(self.carrierLabel, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.previousButton.setText(_translate("Form", "Previous"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.carrierLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))

