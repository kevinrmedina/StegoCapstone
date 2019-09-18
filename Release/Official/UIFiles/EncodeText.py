import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class EncodeText(QtWidgets.QWidget):

    show_Result = QtCore.pyqtSignal(object)
    def ShowResult(self):

        ENCODEDIMAGERESULT = ""                    ####################### Encoded image result goes here, use self.EncodingString
        showResult.emit(ENCODEDIMAGERESULT)
        pass

    def __init__(self, imageData, config, CarrierDir):
        super (EncodeText, self).__init__()
        uic.loadUi('./UIFiles/EncodeText.ui', self)
        self.label = self.findChild(QtWidgets.QLabel, 'carrierImageLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.decodeTextArea = self.findChild(QtWidgets.QTextEdit, 'decodeTextArea')
        self.EncodingString = self.decodeTextArea.toPlainText()         ######### STRING thats going to be encoded ################
        
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'restartButton')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.ShowResult)