from PyQt5 import QtWidgets, uic, QtGui, QtCore
from fileservice import FileService

class ResultScreen(QtWidgets.QWidget):

    switch_mainmenu = QtCore.pyqtSignal()
    switch_previous = QtCore.pyqtSignal(object, object, object, object, object)  # Add switch_window signal for controller to use to switch layouts

    def ShowPrevious(self):
        self.switch_previous.emit(self.imageData, self.config, self.CarrierDir, self.lastPage, self.payloadDir)


    def ShowMainMenu(self):
        self.switch_mainmenu.emit()

    def __init__(self, newDir, imageData, CarrierDir, config, lastPage, payloadDir=None):
        super (ResultScreen, self).__init__()
        uic.loadUi('./UIFiles/ResultScreen.ui', self)
        self.payloadDir = payloadDir
        self.lastPage = lastPage
        self.CarrierDir = CarrierDir
        self.config = config
        self.imageData = imageData
        self.label = self.findChild(QtWidgets.QLabel, 'originalImageLabel')
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageData)
        self.label.setPixmap(pixmap)
        # self.label.resize(pixmap.width(), pixmap.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.label_2 = self.findChild(QtWidgets.QLabel, 'steggedImageLabel')
        pixmap2 = QtGui.QPixmap()
        pixmap2.loadFromData(imageData)
        self.label_2.setPixmap(pixmap2)
        # self.label_2.resize(pixmap.width(), pixmap.height())
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        self.pushButton = self.findChild(QtWidgets.QAbstractButton, 'previousButton')
        # self.pushButton.setText("Next")
        self.pushButton.clicked.connect(self.ShowPrevious)
        self.pushButton_2 = self.findChild(QtWidgets.QAbstractButton, 'mainMenuButton')
        # self.pushButton_2.setText("Next")
        self.pushButton_2.clicked.connect(self.ShowMainMenu)
