# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowsePage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from fileservice import FileService
from PyQt5.QtGui import QPixmap

class BrowsePage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal(object, object)
    
    def __init__(self):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self, imageData): # implement event that will emit the switch window signal 
        self.switch_window.emit(imageData, self.ImageName)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(576, 448)
        Form.setFixedSize(750, 550)
        self.browseFileButton = QtWidgets.QPushButton(Form)
        self.browseFileButton.setGeometry(QtCore.QRect(305, 450, 131, 51))
        self.browseFileButton.setObjectName("browseFileButton")
        self.browseFileButton.clicked.connect(self.OpenBrowseFile)
        self.logoLabel = QtWidgets.QLabel(Form)
        self.logoLabel.setGeometry(QtCore.QRect(140, 0, 471, 401))
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browseFileButton.setText(_translate("Form", "Browse File"))
        self.logoLabel.setText(_translate("Form", "Here goes a picture"))
        pixmap = QPixmap("logo.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.resize(pixmap.width(), pixmap.height())

    def OpenBrowseFile(self):
        ImageFileName = FileService.openFileNameDialog(self.Form, self.Form)
        if (ImageFileName != None and ImageFileName != ""):
            file = FileService.openFileContent(self, ImageFileName)
        else:
            #handle no file warning 
            return
        self.ImageData = file.read()
        self.ImageName = ImageFileName
        self.EmitSwitch(self.ImageData)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
