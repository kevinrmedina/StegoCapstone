from PyQt5.QtWidgets import QFileDialog


##Widget in every method 'widget' is the parent widget which calls file dialog

class FileService:

    def openFileNameDialog(self, widget):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(widget,"QFileDialog.getOpenFileName()", "","*.png", options=options)
        if fileName:
            print(fileName)
        return fileName
    
    def openAnyFileNameDialog(self, widget):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileName(widget,"QFileDialog.getOpenFileName()", "","*", options=options)
        if files:
            print(files)
        return files 
    
    def openFileNamesDialog(self, widget):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(widget,"QFileDialog.getOpenFileNames()", "","*", options=options)
        if files:
            print(files)
        return files 
    def saveFileDialog(self, widget):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(widget,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def openFileContent(self, fileName):
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(widget,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        # if fileName:
        #     print(fileName)
        #QFileDialog.getOpenFileContent("", self.openContentCallback)
        filecontent = open(fileName, 'rb')
        print(filecontent)
        return filecontent

    # def openContentCallback(self, fileName, fileContent):
    #     print(fileName)
    #     print (fileContent)
    

