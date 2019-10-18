import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QPixmap
from fileservice import FileService
from UIFiles.HomePage import HomePage
from UIFiles.BrowsePage import BrowsePage
from UIFiles.EncodeDecodePage import EncodeDecodePage
from UIFiles.ChoosePayloadType import ChoosePayloadTypePage
from UIFiles.translation_pane import TanslationPane
#from UIFiles.EncryptionPage import EncryptionPage
from UIFiles.TextPayloadPage import TextPayloadPage
from UIFiles.EncodeFile import EncodeFile
from UIFiles.DecodeFile import DecodeFile
from UIFiles.DecodeText import DecodeText
from UIFiles.EncodeText import EncodeText
from UIFiles.ResultScreen import ResultScreen
from UIFiles.EncryptDecryptPage import EncryptDecryptPage
from UIFiles.RSAKeyGeneratorPage import RSAKeyGeneratorPage
from UIFiles.hex import Hex_GUI

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
ImageFileName = ""  # used to store image file path and display image in UI


class Controller:
    
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
      
        self.deencodepage = None
        self.encodetext = None
        self.decodefile = None
        self.decodetext = None
        self.encodefile = None
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.home.close()
        self.login.show()

    def show_home(self):
        self.home = HomePage()
        self.MainWindow.setCentralWidget(self.home.Form)
        self.home.switch_window.connect(self.showBrowsePage)
        self.home.show()

    def showBrowsePage(self):
        self.browsepage = BrowsePage()
        self.MainWindow.setCentralWidget(self.browsepage.Form)
        self.browsepage.switch_window.connect(self.ShowDecodeEncodePage)
        try:
            self.home.close()
            self.home = None
        except:
            self.deencodepage.close()
            self.deencodepage = None

        self.browsepage.show()
    
    def ShowDecodeEncodePage(self, imageData, ImageDir):
        self.deencodepage = EncodeDecodePage(imageData, ImageDir)
        self.MainWindow.setCentralWidget(self.deencodepage.Form)
        self.deencodepage.switch_window.connect(self.ShowChoosePayloadTypePage)
        self.deencodepage.previous_clicked.connect(self.showBrowsePage)
        try:
            self.browsepage.close()
            self.browsepage = None
        except:
            self.choosepayload.close()
            self.choosepayload = None
        self.deencodepage.show()

    def ShowChoosePayloadTypePage(self, imageData, config, ImageDir):
        self.choosepayload = ChoosePayloadTypePage(imageData, config, ImageDir)
        self.choosepayload.show_encode_file.connect(self.ShowEncodeFile)
        self.choosepayload.show_decode_file.connect(self.ShowDecodeFile)
        self.choosepayload.show_decode_text.connect(self.ShowDecodeText)
        self.choosepayload.show_encode_text.connect(self.ShowEncodeText)
        self.choosepayload.switch_previous.connect(self.ShowDecodeEncodePage)
        self.MainWindow.setCentralWidget(self.choosepayload.Form)
        if self.deencodepage:
            self.deencodepage.close()
            self.deencodepage = None
        elif self.encodetext:
            self.encodetext.close()
            self.encodetext = None
        elif self.decodefile:
            self.decodefile.close()
            self.decodefile = None
        elif self.decodetext:
            self.decodetext.close()
            self.decodetext = None
        elif self.encodefile:
            self.encodefile.close()
            self.encodefile = None
        
        self.choosepayload.show()
    
    def ShowTextPayloadPage(self, imageData, config, CarrierDir):
        self.textpayload = TextPayloadPage(imageData, config, CarrierDir)
        self.MainWindow.setCentralWidget(self.textpayload.Form)
        self.textpayload.show()
        #self.encryption.close()
        self.choosepayload.close()
    
    def ShowEncodeFile(self, imageData, config, CarrierDir, payloadDir):      
        self.encodefile = EncodeFile(imageData, config, CarrierDir, payloadDir)
        self.MainWindow.setCentralWidget(self.encodefile)
        self.encodefile.show_Result.connect(self.ShowResult)
        self.encodefile.switch_previous.connect(self.ShowChoosePayloadTypePage)
        self.encodefile.show()
        self.choosepayload.close()
     
    def ShowDecodeFile(self, imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey):
        self.decodefile = DecodeFile(imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey)
        self.decodefile.gotoMainMenu.connect(self.show_home)
        self.decodefile.switch_previous.connect(self.ShowChoosePayloadTypePage)
        self.MainWindow.setCentralWidget(self.decodefile)
        self.decodefile.show()
        try:
            self.choosepayload.close()
            self.choosepayload = None
        except:
            pass
    
    def ShowEncodeText(self, imageData, config, CarrierDir, cryptoAlgorithm, password, publicKey):
        self.encodetext = EncodeText(imageData, config, CarrierDir, cryptoAlgorithm, password, publicKey)
        self.encodetext.show_Result.connect(self.ShowResult)
        self.encodetext.switch_previous.connect(self.ShowChoosePayloadTypePage)
        self.MainWindow.setCentralWidget(self.encodetext)
        self.encodetext.show()
        self.choosepayload.close()
    
    def ShowResult(self, EncodedImageResultDir, imageData, CarrierDir, config, lastPage, payloadDir=None):
        self.resultscreen = ResultScreen(EncodedImageResultDir, imageData, CarrierDir, config, lastPage, payloadDir)
        self.resultscreen.switch_mainmenu.connect(self.show_home)
        self.resultscreen.switch_previous.connect(self.ResultGoBack)
        self.MainWindow.setCentralWidget(self.resultscreen)
        self.resultscreen.show()

    def ResultGoBack(self, imageData, config, CarrierDir, lastPage, payloadDir, cryptoAlgorithm):
        if (lastPage == 1):
            self.ShowEncodeFile(imageData, config, CarrierDir, payloadDir)
        elif (lastPage == 2):
            self.ShowDecodeFile(imageData, config, CarrierDir, cryptoAlgorithm)
        elif (lastPage == 3):
            self.ShowEncodeText(imageData, config, CarrierDir, cryptoAlgorithm)
        elif (lastPage == 4):
            self.ShowDecodeText(imageData, config, CarrierDir, cryptoAlgorithm)

    def ShowDecodeText(self, imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey):
        self.decodetext = DecodeText(imageData, config, CarrierDir, cryptoAlgorithm, password, privateKey)
        self.MainWindow.setCentralWidget(self.decodetext)
        self.decodetext.gotoMainMenu.connect(self.show_home)
        self.decodetext.switch_previous.connect(self.ShowChoosePayloadTypePage)
        self.decodetext.show()
        self.choosepayload.close()


    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self, imageData):
        self.window_two = WindowTwo(imageData)
        self.window.close()
        self.window_two.show()

    def OpenTranslationPane(self, randomobjectidontknowabout):
        self.translation = TanslationPane()
        self.translation.show()

    def ShowEncryptDecryptPage(self):
        self.encryptdecrypt = EncryptDecryptPage()
        self.encryptdecrypt.show()

    def ShowRSAKeyGeneratorPage(self):
        self.rsagenerator = RSAKeyGeneratorPage()
        self.rsagenerator.show()
    
    def ShowHexDump(self):
        self.hexdump = Hex_GUI()
        self.hexdump.show()



# Main Execution 
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    controller = Controller(MainWindow)
    #Menu option called Open Translation Pane to 'File' menu
    translationAction = QtWidgets.QAction("Open Translation Pane", MainWindow)
    translationAction.setShortcut("Ctrl+T")
    translationAction.setStatusTip('Open Translation Pane')
    translationAction.triggered.connect(controller.OpenTranslationPane)
    encryptdecryptAction = QtWidgets.QAction("Open Decrypt Encrypt Page", MainWindow)
    encryptdecryptAction.setShortcut("Ctrl+E")
    encryptdecryptAction.setStatusTip('Open decrypt and encrypt page')
    encryptdecryptAction.triggered.connect(controller.ShowEncryptDecryptPage)
    rsageneratorAction = QtWidgets.QAction("Open RSA key generator page", MainWindow)
    rsageneratorAction.setShortcut("Ctrl+K")
    rsageneratorAction.setStatusTip('Open RSA Key generator page')
    rsageneratorAction.triggered.connect(controller.ShowRSAKeyGeneratorPage)
    hexdumpAction = QtWidgets.QAction("Open Hexdump Page", MainWindow)
    hexdumpAction.setShortcut("Ctrl+K")
    hexdumpAction.setStatusTip('Open hex dump page')
    hexdumpAction.triggered.connect(controller.ShowHexDump)

    mainMenu = MainWindow.menuBar()
    toolsMenu = mainMenu.addMenu('&Tools')
    toolsMenu.addAction(translationAction)
    toolsMenu.addAction(encryptdecryptAction)
    toolsMenu.addAction(rsageneratorAction)
    toolsMenu.addAction(hexdumpAction)
    MainWindow.show()
    MainWindow.resize(640, 500)
    #MainWindow.setCentralWidget(self.Form)
    controller.show_home()
    sys.exit(app.exec_())

# Class constructor, only runs main execution
if __name__ == '__main__':
    main()
