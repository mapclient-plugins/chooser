# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label0_3 = QLabel(self.configGroupBox)
        self.label0_3.setObjectName(u"label0_3")

        self.gridLayout_2.addWidget(self.label0_3, 2, 0, 1, 1)

        self.spinBoxFileChoosers = QSpinBox(self.configGroupBox)
        self.spinBoxFileChoosers.setObjectName(u"spinBoxFileChoosers")
        self.spinBoxFileChoosers.setMinimum(0)
        self.spinBoxFileChoosers.setValue(0)

        self.gridLayout_2.addWidget(self.spinBoxFileChoosers, 1, 1, 1, 1)

        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.gridLayout_2.addWidget(self.lineEdit0, 0, 1, 1, 1)

        self.spinBoxDirectoryChoosers = QSpinBox(self.configGroupBox)
        self.spinBoxDirectoryChoosers.setObjectName(u"spinBoxDirectoryChoosers")
        self.spinBoxDirectoryChoosers.setMinimum(0)

        self.gridLayout_2.addWidget(self.spinBoxDirectoryChoosers, 2, 1, 1, 1)

        self.label0_2 = QLabel(self.configGroupBox)
        self.label0_2.setObjectName(u"label0_2")

        self.gridLayout_2.addWidget(self.label0_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        ConfigureDialog.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0_3.setText(QCoreApplication.translate("ConfigureDialog", u"Directory Choosers:", None))
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.label0_2.setText(QCoreApplication.translate("ConfigureDialog", u"File Choosers:", None))
    # retranslateUi

