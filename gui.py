# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(380, 400)
        mainWindow.setMinimumSize(QtCore.QSize(380, 400))
        mainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.saveInfoGroup = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.saveInfoGroup.setFont(font)
        self.saveInfoGroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saveInfoGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.saveInfoGroup.setFlat(False)
        self.saveInfoGroup.setCheckable(False)
        self.saveInfoGroup.setObjectName("saveInfoGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.saveInfoGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(self.saveInfoGroup)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../imgs/save_icon_48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 7, 0, 1, 1)
        self.savesLabel = QtWidgets.QLabel(self.saveInfoGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savesLabel.sizePolicy().hasHeightForWidth())
        self.savesLabel.setSizePolicy(sizePolicy)
        self.savesLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.savesLabel.setFont(font)
        self.savesLabel.setObjectName("savesLabel")
        self.gridLayout.addWidget(self.savesLabel, 0, 0, 1, 4)
        self.savesCombo = QtWidgets.QComboBox(self.saveInfoGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savesCombo.sizePolicy().hasHeightForWidth())
        self.savesCombo.setSizePolicy(sizePolicy)
        self.savesCombo.setMaximumSize(QtCore.QSize(100, 20))
        self.savesCombo.setObjectName("savesCombo")
        self.gridLayout.addWidget(self.savesCombo, 1, 0, 1, 1)
        self.worldGroup = QtWidgets.QGroupBox(self.saveInfoGroup)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.worldGroup.setFont(font)
        self.worldGroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.worldGroup.setAutoFillBackground(False)
        self.worldGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.worldGroup.setFlat(False)
        self.worldGroup.setObjectName("worldGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.worldGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.worldNameLabel = QtWidgets.QLabel(self.worldGroup)
        self.worldNameLabel.setObjectName("worldNameLabel")
        self.gridLayout_2.addWidget(self.worldNameLabel, 0, 0, 1, 2)
        self.worldNameText = QtWidgets.QLineEdit(self.worldGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.worldNameText.sizePolicy().hasHeightForWidth())
        self.worldNameText.setSizePolicy(sizePolicy)
        self.worldNameText.setMaximumSize(QtCore.QSize(90, 20))
        self.worldNameText.setObjectName("worldNameText")
        self.gridLayout_2.addWidget(self.worldNameText, 0, 2, 1, 1)
        self.daysPastLabel = QtWidgets.QLabel(self.worldGroup)
        self.daysPastLabel.setObjectName("daysPastLabel")
        self.gridLayout_2.addWidget(self.daysPastLabel, 1, 0, 1, 1)
        self.daysPastText = QtWidgets.QLineEdit(self.worldGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daysPastText.sizePolicy().hasHeightForWidth())
        self.daysPastText.setSizePolicy(sizePolicy)
        self.daysPastText.setMaximumSize(QtCore.QSize(90, 20))
        self.daysPastText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.daysPastText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.daysPastText.setObjectName("daysPastText")
        self.gridLayout_2.addWidget(self.daysPastText, 1, 2, 1, 1)
        self.researchLabel = QtWidgets.QLabel(self.worldGroup)
        self.researchLabel.setObjectName("researchLabel")
        self.gridLayout_2.addWidget(self.researchLabel, 2, 0, 1, 1)
        self.researchCombo = QtWidgets.QComboBox(self.worldGroup)
        self.researchCombo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.researchCombo.setEditable(False)
        self.researchCombo.setObjectName("researchCombo")
        self.researchCombo.addItem("")
        self.researchCombo.addItem("")
        self.gridLayout_2.addWidget(self.researchCombo, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.worldGroup, 3, 0, 1, 4)
        self.worldSettingsGroup = QtWidgets.QGroupBox(self.saveInfoGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.worldSettingsGroup.sizePolicy().hasHeightForWidth())
        self.worldSettingsGroup.setSizePolicy(sizePolicy)
        self.worldSettingsGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.worldSettingsGroup.setObjectName("worldSettingsGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.worldSettingsGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rotatingSunLabel = QtWidgets.QLabel(self.worldSettingsGroup)
        self.rotatingSunLabel.setObjectName("rotatingSunLabel")
        self.gridLayout_3.addWidget(self.rotatingSunLabel, 0, 0, 1, 1)
        self.rotatingSkyBox = QtWidgets.QComboBox(self.worldSettingsGroup)
        self.rotatingSkyBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.rotatingSkyBox.setObjectName("rotatingSkyBox")
        self.rotatingSkyBox.addItem("")
        self.rotatingSkyBox.addItem("")
        self.gridLayout_3.addWidget(self.rotatingSkyBox, 0, 1, 1, 1)
        self.solarScaleLabel = QtWidgets.QLabel(self.worldSettingsGroup)
        self.solarScaleLabel.setObjectName("solarScaleLabel")
        self.gridLayout_3.addWidget(self.solarScaleLabel, 1, 0, 1, 1)
        self.solarScaleText = QtWidgets.QLineEdit(self.worldSettingsGroup)
        self.solarScaleText.setMaximumSize(QtCore.QSize(90, 20))
        self.solarScaleText.setObjectName("solarScaleText")
        self.gridLayout_3.addWidget(self.solarScaleText, 1, 1, 1, 1)
        self.hungerRateLabel = QtWidgets.QLabel(self.worldSettingsGroup)
        self.hungerRateLabel.setObjectName("hungerRateLabel")
        self.gridLayout_3.addWidget(self.hungerRateLabel, 2, 0, 1, 1)
        self.hungerRateText = QtWidgets.QLineEdit(self.worldSettingsGroup)
        self.hungerRateText.setMaximumSize(QtCore.QSize(90, 20))
        self.hungerRateText.setObjectName("hungerRateText")
        self.gridLayout_3.addWidget(self.hungerRateText, 2, 1, 1, 1)
        self.gravityLabel = QtWidgets.QLabel(self.worldSettingsGroup)
        self.gravityLabel.setObjectName("gravityLabel")
        self.gridLayout_3.addWidget(self.gravityLabel, 3, 0, 1, 1)
        self.gravityText = QtWidgets.QLineEdit(self.worldSettingsGroup)
        self.gravityText.setMaximumSize(QtCore.QSize(90, 20))
        self.gravityText.setObjectName("gravityText")
        self.gridLayout_3.addWidget(self.gravityText, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.worldSettingsGroup, 4, 0, 3, 4)
        self.backupCheck = QtWidgets.QCheckBox(self.saveInfoGroup)
        self.backupCheck.setObjectName("backupCheck")
        self.gridLayout.addWidget(self.backupCheck, 7, 2, 1, 1)
        self.dateModifLabel = QtWidgets.QLabel(self.saveInfoGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateModifLabel.sizePolicy().hasHeightForWidth())
        self.dateModifLabel.setSizePolicy(sizePolicy)
        self.dateModifLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.dateModifLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dateModifLabel.setObjectName("dateModifLabel")
        self.gridLayout.addWidget(self.dateModifLabel, 1, 1, 1, 2)
        self.gridLayout_4.addWidget(self.saveInfoGroup, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Stationeers Save Editor"))
        self.saveInfoGroup.setTitle(_translate("mainWindow", "Save Info"))
        self.saveButton.setText(_translate("mainWindow", "Save file"))
        self.savesLabel.setText(_translate("mainWindow", "TextLabel"))
        self.worldGroup.setTitle(_translate("mainWindow", "world.xml"))
        self.worldNameLabel.setText(_translate("mainWindow", "World Name"))
        self.daysPastLabel.setText(_translate("mainWindow", "Days Past"))
        self.researchLabel.setText(_translate("mainWindow", "Research"))
        self.researchCombo.setCurrentText(_translate("mainWindow", "ResearchOff"))
        self.researchCombo.setItemText(0, _translate("mainWindow", "ResearchOff"))
        self.researchCombo.setItemText(1, _translate("mainWindow", "ResearchOn"))
        self.worldSettingsGroup.setTitle(_translate("mainWindow", "worldsettings.xml"))
        self.rotatingSunLabel.setText(_translate("mainWindow", "Rotating Sky"))
        self.rotatingSkyBox.setItemText(0, _translate("mainWindow", "true"))
        self.rotatingSkyBox.setItemText(1, _translate("mainWindow", "false"))
        self.solarScaleLabel.setText(_translate("mainWindow", "Solar Scale"))
        self.hungerRateLabel.setText(_translate("mainWindow", "Hunger Rate"))
        self.gravityLabel.setText(_translate("mainWindow", "Gravity"))
        self.backupCheck.setText(_translate("mainWindow", "Backup Original Save"))
        self.dateModifLabel.setText(_translate("mainWindow", "TextLabel"))
