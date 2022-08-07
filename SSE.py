from datetime import datetime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import xml.etree.ElementTree as ET
from shutil import copytree
import time
import sys
import gui
from os import environ, path, listdir

class MainForm(QMainWindow, gui.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('imgs/SSE_icon.png'))
        self.savesLabel.setText(self.getPaths()[0])
        self.savesCombo.currentIndexChanged.connect(self.saveChangeSig)
        self.saveButton.clicked.connect(self.rewriteSave)

    def getPaths(self):
        self.myDocsPath = environ.get('USERPROFILE')
        self.savesPath = f'{self.myDocsPath}\\Documents\\My Games\\Stationeers\\saves'
        self.savesFile = f'{self.savesPath}\\{self.savesCombo.currentText()}\\world.xml'
        return self.savesPath, self.savesFile
        

    def getXMLRoot(self):
        xmlTree = ET.parse(self.savesFile)
        rootNode = xmlTree.getroot()
        return xmlTree, rootNode

    def saveChangeSig(self):
        self.dateModifLabel.setText(time.ctime(path.getmtime(self.getPaths()[1])))
        rootNode = self.getXMLRoot()[1]
        for element in rootNode:
            if str(element.tag) == 'ResearchKey':
                self.researchCombo.setCurrentText(element.text)
            elif str(element.tag) == 'DaysPast':
                self.daysPastText.setText(element.text)
            elif str(element.tag) == 'WorldName':
                self.worldNameText.setText(element.text)

    def rewriteSave(self):
        xmlTree = self.getXMLRoot()[0]
        xmlTree.find('.//ResearchKey').text = self.researchCombo.currentText()
        xmlTree.find('.//DaysPast').text = self.daysPastText.text()
        dateformat = '%Y_%m_%d_%H_%M_%S'
        if self.backupCheck.isChecked():
            copytree(f'{self.getPaths()[0]}\\{self.savesCombo.currentText()}',
                     f'{self.getPaths()[0]}\\{self.savesCombo.currentText()}_{datetime.now().strftime(dateformat)}')
        xmlTree.write(f'{self.savesFile}')
        msgbox('Save File modified!')

def msgbox(mText):
    mBox = QMessageBox()
    mBox.setWindowTitle('Info')
    mBox.setText(mText)
    mBox.setIcon(QMessageBox.Information)
    popupWindow = mBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    for i in (listdir(form.savesPath)):
        if path.isdir(f'{form.savesPath}\\{i}'):
            form.savesCombo.addItem(str(i))
    app.exec()