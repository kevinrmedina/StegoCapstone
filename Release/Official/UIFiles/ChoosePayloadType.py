# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/ChooseCarrierType.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from fileservice import FileService 
from PyQt5 import QtCore, QtGui, QtWidgets


class ChoosePayloadTypePage(QtCore.QObject):

    show_encode_file = QtCore.pyqtSignal(object, object, object, object)  # Add switch_window signal for controller to use to switch layouts
    switch_previous = QtCore.pyqtSignal(object, object)  # Add switch_window signal for controller to use to switch layouts
    show_encode_text = QtCore.pyqtSignal(object, object, object)
    show_decode_text = QtCore.pyqtSignal(object, object, object)
    show_decode_file = QtCore.pyqtSignal(object, object, object)
    def __init__(self, imageData, config, CarrierDir):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        self.imagedata = imageData
        self.carrierDir = CarrierDir
        self.Config = config
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitchNext(self): # implement event that will emit the switch window signal 
        if (self.Config == "Encode"):
            if (self.radioButton_2.isChecked()):
                #Show Browser to select payload and pass it to next page (pass payload directory)
                payloadDir = FileService.openFileNameDialog(self.Form, self.Form)
                self.show_encode_file.emit(self.imagedata, self.Config, self.carrierDir, payloadDir)
            else:
                self.show_encode_text.emit(self.imagedata, self.Config, self.carrierDir)
        else:
            if (self.radioButton_2.isChecked()):
                self.show_decode_file.emit(self.imagedata, self.Config, self.carrierDir)
            else:
                self.show_decode_text.emit(self.imagedata, self.Config, self.carrierDir)
    
    def EmitSwitchPrevious(self): # implement event that will emit the switch window signal 
        self.switch_previous.emit(self.imagedata, self.carrierDir)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(639, 550)
        Form.setFixedSize(750, 550)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 201, 272))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton.setChecked(True)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox.clicked.connect(self.checkBoxClicked)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.comboBox_3.setEnabled(False)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit.setEnabled(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(388, 80, 221, 271))
        # self.label.setText("")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.imagedata)
        self.label.setPixmap(pixmap)
        # self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 370, 221, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.clicked.connect(self.EmitSwitchPrevious)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.EmitSwitchNext)
        self.ActionLabel = QtWidgets.QLabel(Form)
        self.ActionLabel.setGeometry(QtCore.QRect(20, 20, 611, 20))
        self.ActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ActionLabel.setObjectName("ActionLabel")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "Text"))
        self.radioButton_2.setText(_translate("Form", "File"))
        self.checkBox.setText(_translate("Form", "Cryptography"))
        self.plainTextEdit.setPlainText(_translate("Form", "Encryption Key\n"
""))
        self.pushButton_2.setText(_translate("Form", "Prev"))
        self.pushButton.setText(_translate("Form", "Next"))
        self.ActionLabel.setText(_translate("Form", self.Config))

    def checkBoxClicked(self):
        if (self.checkBox.isChecked()):
            self.comboBox_3.setEnabled(True)
            self.plainTextEdit.setEnabled(True)
        else:
            self.comboBox_3.setEnabled(False)
            self.plainTextEdit.setEnabled(False)
