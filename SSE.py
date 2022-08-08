from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from yaml import full_load as loadyaml
from os import environ, path, listdir
from datetime import datetime
from shutil import copytree
import xml.etree.ElementTree as ET
import time
import sys
import gui

class MainForm(QMainWindow, gui.Ui_mainWindow):
    """Создание графического интерфейса.

    Args:
        QMainWindow: Главное окно программы
        gui: Конфигурация окна
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('imgs/SSE_icon.ico'))
        self.saveButton.setIcon(QIcon('imgs/save_icon_16.ico'))
        self.savesLabel.setText(self.getPaths()[0])
        self.savesCombo.currentIndexChanged.connect(self.saveChangeSig)
        self.saveButton.clicked.connect(self.rewriteSave)
        self.statusBar.showMessage(f'v.: {buildInfo()[0]}, by {buildInfo()[1]} ({buildInfo()[2]})')

    def getPaths(self) -> list:
        """Определяет основные пути до сохранения.

        Returns:
            list: Список путей c директорией сохранения и до самого файла world.xml
        """
        self.myDocsPath = environ.get('USERPROFILE')
        self.savePath = f'{self.myDocsPath}\\Documents\\My Games\\Stationeers\\saves'
        self.saveWorld = f'{self.savePath}\\{self.savesCombo.currentText()}\\world.xml'
        self.saveWorldS = f'{self.savePath}\\{self.savesCombo.currentText()}\\worldsettings.xml'
        return self.savePath, self.saveWorld, self.saveWorldS
        

    def getXML(self) -> list:
        """Парсит XML конфиг.

        Returns:
            list: Список с деревом XML и с корневым элементом
        """
        worldXMLTree = ET.parse(self.saveWorld)
        worldRootNode = worldXMLTree.getroot()
        worldSXMLTree = ET.parse(self.saveWorldS)
        worldSRootNode = worldSXMLTree.getroot()
        return worldXMLTree, worldRootNode, worldSXMLTree, worldSRootNode

    def saveChangeSig(self):
        """Обработка события смены редактируемого сейва.
        """
        self.dateModifLabel.setText(time.ctime(path.getmtime(self.getPaths()[1])))
        w_rootNode = self.getXML()[1]
        ws_rootNode = self.getXML()[3]
        for element in w_rootNode:
            if str(element.tag) == 'ResearchKey':
                self.researchCombo.setCurrentText(element.text)
            elif str(element.tag) == 'DaysPast':
                self.daysPastText.setText(element.text)
            elif str(element.tag) == 'WorldName':
                self.worldNameText.setText(element.text)
        for element in ws_rootNode:
            if str(element.tag) == 'Gravity':
                self.gravityText.setText(element.text)
            elif str(element.tag) == 'HungerRate':
                self.hungerRateText.setText(element.text)
            elif str(element.tag) == 'SolarScale':
                self.solarScaleText.setText(element.text)
            elif str(element.tag) == 'RotatingSky':
                self.rotatingSkyBox.setCurrentText(element.text)

    def rewriteSave(self):
        """Обработка сохранения отредактированного сейва.
        """
        wXMLTree = self.getXML()[0]
        wXMLTree.find('.//ResearchKey').text = self.researchCombo.currentText()
        wXMLTree.find('.//DaysPast').text = self.daysPastText.text()
        wsXMLTree = self.getXML()[2]
        wsXMLTree.find('.//Gravity').text = self.gravityText.text()
        wsXMLTree.find('.//HungerRate').text = self.hungerRateText.text()
        wsXMLTree.find('.//SolarScale').text = self.solarScaleText.text()
        wsXMLTree.find('.//RotatingSky').text = self.rotatingSkyBox.currentText()
        dateformat = '%Y_%m_%d_%H_%M_%S'
        if self.backupCheck.isChecked():
            copytree(f'{self.getPaths()[0]}\\{self.savesCombo.currentText()}',
                     f'{self.getPaths()[0]}\\{self.savesCombo.currentText()}_{datetime.now().strftime(dateformat)}')
        wXMLTree.write(self.saveWorld)
        wsXMLTree.write(self.saveWorldS)
        msgbox('Save File modified!')

def msgbox(mText: str):
    """Вызывает информационное окно с результатом операции.

    Args:
        mText (string): Строка для отображения во всплывающем окне
    """
    mBox = QMessageBox()
    mBox.setWindowTitle('Info')
    mBox.setText(mText)
    mBox.setIcon(QMessageBox.Information)
    mBox.exec_()

def buildInfo() -> list:
    """Выводит информацию о версии в статусбаре.

    Returns:
        list: Список данных о версии и авторе
    """
    with open('config.yaml', 'r') as config:
        progAbout = loadyaml(config)
    return progAbout['main']['version'], progAbout['main']['author'], progAbout['main']['authorlink']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    for i in (listdir(form.savePath)):
        if path.isdir(f'{form.savePath}\\{i}'):
            form.savesCombo.addItem(str(i))
    app.exec()