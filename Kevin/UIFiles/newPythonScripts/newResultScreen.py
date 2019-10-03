# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 550)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 430, 181, 41))
        self.label_4.setObjectName("label_4")
        self.restartButton = QtWidgets.QPushButton(Form)
        self.restartButton.setGeometry(QtCore.QRect(560, 470, 113, 51))
        self.restartButton.setObjectName("restartButton")
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setGeometry(QtCore.QRect(430, 470, 113, 51))
        self.previousButton.setObjectName("previousButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 430, 181, 41))
        self.label_3.setObjectName("label_3")
        self.steggedImageScrollArea = QtWidgets.QScrollArea(Form)
        self.steggedImageScrollArea.setGeometry(QtCore.QRect(10, 10, 349, 419))
        self.steggedImageScrollArea.setWidgetResizable(True)
        self.steggedImageScrollArea.setObjectName("steggedImageScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 347, 417))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.steggedImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.steggedImageLabel.setObjectName("steggedImageLabel")
        self.gridLayout_3.addWidget(self.steggedImageLabel, 0, 0, 1, 1)
        self.steggedImageScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.originalImageScrollArea = QtWidgets.QScrollArea(Form)
        self.originalImageScrollArea.setGeometry(QtCore.QRect(390, 10, 349, 419))
        self.originalImageScrollArea.setWidgetResizable(True)
        self.originalImageScrollArea.setObjectName("originalImageScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 347, 417))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.originalImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.originalImageLabel.setObjectName("originalImageLabel")
        self.gridLayout_4.addWidget(self.originalImageLabel, 0, 0, 1, 1)
        self.originalImageScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Original Image"))
        self.restartButton.setText(_translate("Form", "Restart"))
        self.previousButton.setText(_translate("Form", "Previous"))
        self.label_3.setText(_translate("Form", "Stegged Image"))
        self.steggedImageLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))
        self.originalImageLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))

