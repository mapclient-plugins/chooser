# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Thu Jun 11 11:28:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label0_3 = QtGui.QLabel(self.configGroupBox)
        self.label0_3.setObjectName("label0_3")
        self.gridLayout_2.addWidget(self.label0_3, 2, 0, 1, 1)
        self.spinBoxFileChoosers = QtGui.QSpinBox(self.configGroupBox)
        self.spinBoxFileChoosers.setMinimum(0)
        self.spinBoxFileChoosers.setProperty("value", 0)
        self.spinBoxFileChoosers.setObjectName("spinBoxFileChoosers")
        self.gridLayout_2.addWidget(self.spinBoxFileChoosers, 1, 1, 1, 1)
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.gridLayout_2.addWidget(self.lineEdit0, 0, 1, 1, 1)
        self.spinBoxDirectoryChoosers = QtGui.QSpinBox(self.configGroupBox)
        self.spinBoxDirectoryChoosers.setMinimum(0)
        self.spinBoxDirectoryChoosers.setObjectName("spinBoxDirectoryChoosers")
        self.gridLayout_2.addWidget(self.spinBoxDirectoryChoosers, 2, 1, 1, 1)
        self.label0_2 = QtGui.QLabel(self.configGroupBox)
        self.label0_2.setObjectName("label0_2")
        self.gridLayout_2.addWidget(self.label0_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(ConfigureDialog, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "ConfigureDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label0_3.setText(QtGui.QApplication.translate("ConfigureDialog", "Directory Choosers:", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label0_2.setText(QtGui.QApplication.translate("ConfigureDialog", "File Choosers:", None, QtGui.QApplication.UnicodeUTF8))

