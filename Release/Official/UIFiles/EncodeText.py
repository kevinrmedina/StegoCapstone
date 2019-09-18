import sys
from PyQt5 import QtWidgets, uic, QtGui

class EncodeText(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (EncodeText, self).__init__()
        uic.loadUi('./UIFiles/EncodeText.ui', self)