import sys
from PyQt5 import QtWidgets, uic, QtGui

class DecodeText(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (DecodeText, self).__init__()
        uic.loadUi('./UIFiles/DecodeText.ui', self)
        self.label = self.findChild(QtWidgets.QLabel, 'carrierImageLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.decodeTextArea = self.findChild(QtWidgets.QTextEdit, 'decodeTextArea')
        DECODEDTEXT = ""                                            ######### Decoded text goes here ################
        self.decodeTextArea.setPlainText(DECODEDTEXT)
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'pushButton_2')
        self.pushButton_2.setText("Restart")
        self.pushButton_2.clicked.connect(self.RestartDecode)