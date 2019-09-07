# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeDecodePage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EncodeDecodePage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal(object, object)  # Add switch_window signal for controller to use to switch layouts
    def __init__(self, ImageData):
        QtCore.QObject.__init__(self) # call init from parent class
        self.imagedata = ImageData
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self): # implement event that will emit the switch window signal
        config = "Encode/Decode" 
        if (self.radioButton_2.isChecked()):
            config = "Encode"
        else:
            config = "Decode"
        self.switch_window.emit(self.imagedata, config)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 495)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 111, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(True)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 70, 251, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.imagedata)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 390, 221, 80))
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
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.EmitSwitch)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton_2.setText(_translate("Form", "Encode"))
        self.radioButton.setText(_translate("Form", "Decode"))
        #self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "Prev"))
        self.pushButton.setText(_translate("Form", "Next"))