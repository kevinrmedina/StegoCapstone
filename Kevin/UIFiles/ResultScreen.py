from PyQt5 import QtWidgets, uic, QtGui, QtCore
from fileservice import FileService

class ResultScreen(QtWidgets.QWidget):

    switch_mainmenu = QtCore.pyqtSignal()
    switch_previous = QtCore.pyqtSignal(object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def ShowPrevious(self):
        switch_previous.emit(self.imageData, self.config, self.CarrierDir, self.lastPage, self.payloadDir)

    def ShowMainMenu(self):
        switch_mainmenu.emit()

    def __init__(self, newDir, imageData, CarrierDir, config, lastPage, payloadDir=None):
        super (ResultScreen, self).__init__()
        uic.loadUi('./UIFiles/ResultScreen.ui', self)
        if (payloadDir != None):
            self.payloadDir = payloadDir
        self.lastPage = lastPage
        self.CarrierDir = CarrierDir
        self.config = config
        self.imageData = imageData
        self.label = self.findChild(QtWidgets.QLabel, 'carrierLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        # self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'resultLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label_2.setPixmap(pixmap)
        # self.label_2.resize(pixmap.width(), pixmap.height())
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
