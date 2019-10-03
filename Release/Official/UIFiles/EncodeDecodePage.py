# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeDecodePage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EncodeDecodePage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts
    previous_clicked = QtCore.pyqtSignal()
    def __init__(self, ImageData, ImageDir):
        QtCore.QObject.__init__(self) # call init from parent class
        self.imagedata = ImageData
        self.imagedir = ImageDir
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self): # implement event that will emit the switch window signal
        config = "Encode/Decode" 
        if (self.encodeRadioButton.isChecked()):
            config = "Encode"
        else:
            config = "Decode"
        self.switch_window.emit(self.imagedata, config, self.imagedir)
    
    def PreviousButtonClicked(self):
        self.previous_clicked.emit()
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(638, 495)
        Form.setFixedSize(750, 550)
        #self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 111, 291))
        #self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        #self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout.setObjectName("verticalLayout")
        #self.encodeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        #self.encodeRadioButton.setObjectName("encodeRadioButton")
        #self.encodeRadioButton.setChecked(True)
        #self.verticalLayout.addWidget(self.encodeRadioButton)
        #self.decodeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        #self.decodeRadioButton.setObjectName("decodeRadioButton")
        #self.verticalLayout.addWidget(self.decodeRadioButton)
        #self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        #self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 70, 251, 301))
        #self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        #self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        #self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.label.setObjectName("label")
        #pixmap = QtGui.QPixmap()
        #pixmap.loadFromData(self.imagedata)
        #self.label.setPixmap(pixmap)
        #self.label.resize(pixmap.width(), pixmap.height())
        #self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        #self.label.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
        #self.verticalLayout_2.addWidget(self.label)
        #self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        #self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 390, 221, 80))
        #self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        #self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        #self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        #self.horizontalLayout.setObjectName("horizontalLayout")
        #self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        #self.nextButton.setSizePolicy(sizePolicy)
        #self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        #self.nextButton.setObjectName("nextButton")
        #self.horizontalLayout.addWidget(self.nextButton)
        #self.nextButton.clicked.connect(self.PreviousButtonClicked)
        #self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        #self.previousButton.setMinimumSize(QtCore.QSize(0, 50))
        #self.previousButton.setObjectName("previousButton")
        #self.horizontalLayout.addWidget(self.previousButton)
        #self.previousButton.clicked.connect(self.EmitSwitch)
        #self.retranslateUi(Form)
        #QtCore.QMetaObject.connectSlotsByName(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 120, 111, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encodeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.encodeRadioButton.setObjectName("encodeRadioButton")
        self.verticalLayout.addWidget(self.encodeRadioButton)
        self.encodeRadioButton.setChecked(True)
        self.decodeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.decodeRadioButton.setObjectName("decodeRadioButton")
        self.verticalLayout.addWidget(self.decodeRadioButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 460, 221, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setMinimumSize(QtCore.QSize(0, 50))
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.previousButton.clicked.connect(self.PreviousButtonClicked)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.EmitSwitch)
        self.horizontalLayout.addWidget(self.nextButton)
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(370, 10, 370, 450))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 368, 448))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.carrierLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carrierLabel.setObjectName("carrierLabel")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.imagedata)
        self.carrierLabel.setPixmap(pixmap)
        self.gridLayout_3.addWidget(self.carrierLabel, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.encodeRadioButton.setText(_translate("Form", "Encode"))
        self.decodeRadioButton.setText(_translate("Form", "Decode"))
        #self.label.setText(_translate("Form", "TextLabel"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.previousButton.setText(_translate("Form", "Previous"))
