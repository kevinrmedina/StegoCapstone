# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowsePage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from fileservice import FileService


class BrowsePage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal(object)
    
    def __init__(self):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self, imageData): # implement event that will emit the switch window signal 
        self.switch_window.emit(imageData)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 448)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 300, 89, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.OpenBrowseFile)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 50, 171, 151))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Browse File"))
        self.label.setText(_translate("Form", "Here goes a picture "))

    def OpenBrowseFile(self):
        ImageFileName = FileService.openFileNameDialog(self.Form, self.Form, "")
        if (ImageFileName != None or ImageFileName != ""):
            file = FileService.openFileContent(self, ImageFileName)
        else:
            #handle no file warning 
            return
        self.ImageData = file.read()
        self.EmitSwitch(self.ImageData)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
