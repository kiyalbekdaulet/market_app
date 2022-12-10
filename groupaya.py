# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupaya.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_CoordWidget(object):
    def setupUi(self, CoordWidget):
        if not CoordWidget.objectName():
            CoordWidget.setObjectName(u"CoordWidget")
        CoordWidget.resize(1004, 429)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CoordWidget.sizePolicy().hasHeightForWidth())
        CoordWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        CoordWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(CoordWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CoordWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_product = QLabel(self.groupBox)
        self.image_product.setObjectName(u"image_product")
        self.image_product.setMinimumSize(QSize(500, 350))
        self.image_product.setMaximumSize(QSize(600, 400))
        self.image_product.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.image_product.setScaledContents(True)

        self.horizontalLayout.addWidget(self.image_product)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_filter_name = QLabel(self.frame)
        self.label_filter_name.setObjectName(u"label_filter_name")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        self.label_filter_name.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_filter_name)

        self.label_filter_price = QLabel(self.frame)
        self.label_filter_price.setObjectName(u"label_filter_price")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Thin"])
        font2.setPointSize(12)
        font2.setItalic(True)
        self.label_filter_price.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_filter_price)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_clear = QPushButton(self.groupBox)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(r"C:\Users\Sherlock Holmes\PycharmProjects\\final\icons/basket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon)
        self.btn_clear.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_clear)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(CoordWidget)

        QMetaObject.connectSlotsByName(CoordWidget)
    # setupUi

    def retranslateUi(self, CoordWidget):
        CoordWidget.setWindowTitle(QCoreApplication.translate("CoordWidget", u"Form", None))
        self.image_product.setText("")
        self.label_filter_name.setText(QCoreApplication.translate("CoordWidget", u"TextLabel", None))
        self.label_filter_price.setText(QCoreApplication.translate("CoordWidget", u"TextLabel", None))
        self.btn_clear.setText("")
    # retranslateUi

