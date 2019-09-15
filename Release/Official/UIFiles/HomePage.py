# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


###########################
# This class may serve as an example on how to setup a .py file generated from a .ui file to be compatible 
# with our code architecture
#
#The comments in the code shows the minimum requirements for the code to be compatible with the Controller class
###########################

class HomePage(QtCore.QObject):   # inherit class from QObject rather than object to be able to emit signals
    
    switch_window = QtCore.pyqtSignal()  # Add switch_window signal for controller to use to switch layouts
    def __init__(self):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self): # implement event that will emit the switch window signal 
        self.switch_window.emit()
    
    def close(self): # implement close method used by controller
        self.Form.close()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(658, 478)
        Form.setFixedSize(750, 550)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(18, 20, 631, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 70, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.EmitSwitch) # Add event to button that switches window to another layout
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Home Page")) # Change title to your liking
        self.label.setText(_translate("Form", "Available Applications "))
        self.pushButton.setText(_translate("Form", "Steganography"))
