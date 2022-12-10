# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1224, 773)
        MainWindow.setStyleSheet(u"background-color: rgb(31, 42, 58);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_filter = QPushButton(self.frame)
        self.btn_filter.setObjectName(u"btn_filter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.btn_filter.sizePolicy().hasHeightForWidth())
        self.btn_filter.setSizePolicy(sizePolicy1)
        self.btn_filter.setMinimumSize(QSize(50, 50))
        self.btn_filter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filter.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(r"C:\Users\Sherlock Holmes\PycharmProjects\\final\icons/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filter.setIcon(icon)
        self.btn_filter.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_filter)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit_search = QLineEdit(self.frame)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(0, 55))
        self.lineEdit_search.setMaximumSize(QSize(16777215, 55))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setStyleSheet(u"QLineEdit {\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 0px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"\n"
"	border: 4px solid rgb(48, 50, 62);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(244, 104, 104);}")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(55, 55))
        self.btn_search.setMaximumSize(QSize(55, 55))
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 20px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 4px solid rgb(48, 50, 62);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(r"C:\Users\Sherlock Holmes\PycharmProjects\\final\icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_search)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_basket = QPushButton(self.frame)
        self.btn_basket.setObjectName(u"btn_basket")
        self.btn_basket.setMinimumSize(QSize(50, 50))
        self.btn_basket.setMaximumSize(QSize(50, 50))
        self.btn_basket.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_basket.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(r"C:\Users\Sherlock Holmes\PycharmProjects\\final\icons/basket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_basket.setIcon(icon2)
        self.btn_basket.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_basket)

        self.btn_profile = QPushButton(self.frame)
        self.btn_profile.setObjectName(u"btn_profile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_profile.sizePolicy().hasHeightForWidth())
        self.btn_profile.setSizePolicy(sizePolicy2)
        self.btn_profile.setMinimumSize(QSize(50, 50))
        self.btn_profile.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_profile.setFont(font1)
        self.btn_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_profile.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(244, 104, 104);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_profile)


        self.verticalLayout.addWidget(self.frame)

        self.center_main_items = QFrame(self.centralwidget)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.all_products_page = QWidget()
        self.all_products_page.setObjectName(u"all_products_page")
        self.verticalLayout_3 = QVBoxLayout(self.all_products_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.all_products_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1154, 546))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.add_all_product = QVBoxLayout()
        self.add_all_product.setObjectName(u"add_all_product")

        self.verticalLayout_5.addLayout(self.add_all_product)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.all_products_page)
        self.info_product = QWidget()
        self.info_product.setObjectName(u"info_product")
        self.verticalLayout_4 = QVBoxLayout(self.info_product)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_23 = QFrame(self.info_product)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 0))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_24)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_image_to_buy = QLabel(self.frame_24)
        self.label_image_to_buy.setObjectName(u"label_image_to_buy")
        self.label_image_to_buy.setMinimumSize(QSize(600, 0))
        self.label_image_to_buy.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_image_to_buy.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_image_to_buy)

        self.label_info_price = QLabel(self.frame_24)
        self.label_info_price.setObjectName(u"label_info_price")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_info_price.sizePolicy().hasHeightForWidth())
        self.label_info_price.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Montserrat SemiBold"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_info_price.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_info_price)


        self.horizontalLayout_26.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_25)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_3 = QScrollArea(self.frame_25)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 384, 757))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_26 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_36 = QFrame(self.frame_26)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_42 = QLabel(self.frame_36)
        self.label_42.setObjectName(u"label_42")
        font3 = QFont()
        font3.setFamilies([u"Montserrat SemiBold"])
        font3.setPointSize(12)
        self.label_42.setFont(font3)

        self.horizontalLayout_45.addWidget(self.label_42)

        self.label_info_name = QLabel(self.frame_36)
        self.label_info_name.setObjectName(u"label_info_name")
        font4 = QFont()
        font4.setFamilies([u"Montserrat Light"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_info_name.setFont(font4)
        self.label_info_name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_45.addWidget(self.label_info_name)


        self.verticalLayout_16.addWidget(self.frame_36)

        self.frame_46 = QFrame(self.frame_26)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_44 = QLabel(self.frame_46)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.horizontalLayout_46.addWidget(self.label_44)

        self.label_info_win = QLabel(self.frame_46)
        self.label_info_win.setObjectName(u"label_info_win")
        self.label_info_win.setFont(font4)
        self.label_info_win.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_46.addWidget(self.label_info_win)


        self.verticalLayout_16.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_26)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_46 = QLabel(self.frame_47)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.horizontalLayout_47.addWidget(self.label_46)

        self.label_info_proc = QLabel(self.frame_47)
        self.label_info_proc.setObjectName(u"label_info_proc")
        self.label_info_proc.setFont(font4)
        self.label_info_proc.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_47.addWidget(self.label_info_proc)


        self.verticalLayout_16.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_26)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_48 = QLabel(self.frame_48)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)

        self.horizontalLayout_48.addWidget(self.label_48)

        self.label_info_mb = QLabel(self.frame_48)
        self.label_info_mb.setObjectName(u"label_info_mb")
        self.label_info_mb.setFont(font4)
        self.label_info_mb.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_48.addWidget(self.label_info_mb)


        self.verticalLayout_16.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_26)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_50 = QLabel(self.frame_49)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.horizontalLayout_49.addWidget(self.label_50)

        self.label_info_video = QLabel(self.frame_49)
        self.label_info_video.setObjectName(u"label_info_video")
        self.label_info_video.setFont(font4)
        self.label_info_video.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_49.addWidget(self.label_info_video)


        self.verticalLayout_16.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_26)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_52 = QLabel(self.frame_50)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.horizontalLayout_50.addWidget(self.label_52)

        self.label_info_ozu = QLabel(self.frame_50)
        self.label_info_ozu.setObjectName(u"label_info_ozu")
        self.label_info_ozu.setFont(font4)
        self.label_info_ozu.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_50.addWidget(self.label_info_ozu)


        self.verticalLayout_16.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_26)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_54 = QLabel(self.frame_51)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.horizontalLayout_51.addWidget(self.label_54)

        self.label_info_ssd = QLabel(self.frame_51)
        self.label_info_ssd.setObjectName(u"label_info_ssd")
        self.label_info_ssd.setFont(font4)
        self.label_info_ssd.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_51.addWidget(self.label_info_ssd)


        self.verticalLayout_16.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_26)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_56 = QLabel(self.frame_52)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)

        self.horizontalLayout_52.addWidget(self.label_56)

        self.label_info_hdd = QLabel(self.frame_52)
        self.label_info_hdd.setObjectName(u"label_info_hdd")
        self.label_info_hdd.setFont(font4)
        self.label_info_hdd.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_52.addWidget(self.label_info_hdd)


        self.verticalLayout_16.addWidget(self.frame_52)

        self.frame_54 = QFrame(self.frame_26)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_57 = QLabel(self.frame_54)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)

        self.horizontalLayout_55.addWidget(self.label_57)

        self.label_info_block = QLabel(self.frame_54)
        self.label_info_block.setObjectName(u"label_info_block")
        self.label_info_block.setFont(font4)
        self.label_info_block.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_55.addWidget(self.label_info_block)


        self.verticalLayout_16.addWidget(self.frame_54)

        self.frame_57 = QFrame(self.frame_26)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_60 = QLabel(self.frame_57)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)

        self.horizontalLayout_58.addWidget(self.label_60)

        self.label_info_cp = QLabel(self.frame_57)
        self.label_info_cp.setObjectName(u"label_info_cp")
        self.label_info_cp.setFont(font4)
        self.label_info_cp.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_58.addWidget(self.label_info_cp)


        self.verticalLayout_16.addWidget(self.frame_57)

        self.frame_56 = QFrame(self.frame_26)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_59 = QLabel(self.frame_56)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)

        self.horizontalLayout_57.addWidget(self.label_59)

        self.label_info_cc = QLabel(self.frame_56)
        self.label_info_cc.setObjectName(u"label_info_cc")
        self.label_info_cc.setFont(font4)
        self.label_info_cc.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_57.addWidget(self.label_info_cc)


        self.verticalLayout_16.addWidget(self.frame_56)

        self.frame_53 = QFrame(self.frame_26)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalSpacer_17 = QSpacerItem(394, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_17)

        self.btn_info_buy = QPushButton(self.frame_53)
        self.btn_info_buy.setObjectName(u"btn_info_buy")
        self.btn_info_buy.setMinimumSize(QSize(300, 0))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.btn_info_buy.setFont(font5)
        self.btn_info_buy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info_buy.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	padding-left: 60px;\n"
"	padding-right: 60px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")

        self.horizontalLayout_53.addWidget(self.btn_info_buy)

        self.horizontalSpacer_18 = QSpacerItem(394, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_18)


        self.verticalLayout_16.addWidget(self.frame_53)


        self.verticalLayout_17.addWidget(self.frame_26)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_15.addWidget(self.scrollArea_3)


        self.horizontalLayout_26.addWidget(self.frame_25)


        self.verticalLayout_4.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.info_product)
        self.filter_page = QWidget()
        self.filter_page.setObjectName(u"filter_page")
        self.horizontalLayout_2 = QHBoxLayout(self.filter_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.frame_2 = QFrame(self.filter_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMaximumSize(QSize(800, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 255, 133);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"Montserrat"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label.setFont(font6)

        self.verticalLayout_10.addWidget(self.label)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_5)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_11)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_filter_from = QLineEdit(self.frame_7)
        self.lineEdit_filter_from.setObjectName(u"lineEdit_filter_from")
        font7 = QFont()
        font7.setFamilies([u"Montserrat Medium"])
        font7.setPointSize(12)
        self.lineEdit_filter_from.setFont(font7)
        self.lineEdit_filter_from.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 20px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);}\n"
"QLineEdit:focus{\n"
"\n"
"	border: 2px solid rgb(244, 104, 104);}")
        self.lineEdit_filter_from.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_5.addWidget(self.lineEdit_filter_from)

        self.lineEdit_filter_before = QLineEdit(self.frame_7)
        self.lineEdit_filter_before.setObjectName(u"lineEdit_filter_before")
        font8 = QFont()
        font8.setFamilies([u"Montserrat Medium"])
        font8.setPointSize(12)
        font8.setBold(False)
        self.lineEdit_filter_before.setFont(font8)
        self.lineEdit_filter_before.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 20px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(244, 104, 104);}")
        self.lineEdit_filter_before.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_5.addWidget(self.lineEdit_filter_before)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBox_filter_brand = QComboBox(self.frame_8)
        self.comboBox_filter_brand.setObjectName(u"comboBox_filter_brand")
        self.comboBox_filter_brand.setFont(font3)
        self.comboBox_filter_brand.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.comboBox_filter_brand)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comboBox_filter_ram = QComboBox(self.frame_9)
        self.comboBox_filter_ram.setObjectName(u"comboBox_filter_ram")
        self.comboBox_filter_ram.setFont(font3)
        self.comboBox_filter_ram.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.comboBox_filter_ram)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox_filter_proc = QComboBox(self.frame_10)
        self.comboBox_filter_proc.setObjectName(u"comboBox_filter_proc")
        self.comboBox_filter_proc.setFont(font3)
        self.comboBox_filter_proc.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_14.addWidget(self.comboBox_filter_proc)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_filter_win = QComboBox(self.frame_12)
        self.comboBox_filter_win.setObjectName(u"comboBox_filter_win")
        self.comboBox_filter_win.setFont(font3)
        self.comboBox_filter_win.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.comboBox_filter_win)


        self.verticalLayout_11.addWidget(self.frame_12)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_6)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_filter_search = QPushButton(self.frame_13)
        self.btn_filter_search.setObjectName(u"btn_filter_search")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_filter_search.sizePolicy().hasHeightForWidth())
        self.btn_filter_search.setSizePolicy(sizePolicy4)
        self.btn_filter_search.setFont(font5)
        self.btn_filter_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filter_search.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 60px;\n"
"	padding-right: 60px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: rgb(244, 104, 104);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_filter_search)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_13)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.stackedWidget.addWidget(self.filter_page)
        self.basket_page = QWidget()
        self.basket_page.setObjectName(u"basket_page")
        self.verticalLayout_6 = QVBoxLayout(self.basket_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.basket_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1130, 442))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.basket_all_product = QVBoxLayout()
        self.basket_all_product.setObjectName(u"basket_all_product")

        self.horizontalLayout_4.addLayout(self.basket_all_product)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_basket_all_clear = QPushButton(self.frame_4)
        self.btn_basket_all_clear.setObjectName(u"btn_basket_all_clear")
        sizePolicy5.setHeightForWidth(self.btn_basket_all_clear.sizePolicy().hasHeightForWidth())
        self.btn_basket_all_clear.setSizePolicy(sizePolicy5)
        self.btn_basket_all_clear.setMinimumSize(QSize(250, 0))
        self.btn_basket_all_clear.setFont(font5)
        self.btn_basket_all_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_basket_all_clear.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 60px;\n"
"	padding-right: 60px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: rgb(244, 104, 104);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_basket_all_clear)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.basket_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_9 = QVBoxLayout(self.profile_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.profile_page)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_11)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        font9 = QFont()
        font9.setFamilies([u"Montserrat SemiBold"])
        font9.setPointSize(16)
        font9.setBold(False)
        self.label_17.setFont(font9)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.label_profile_name = QLabel(self.frame_19)
        self.label_profile_name.setObjectName(u"label_profile_name")
        sizePolicy3.setHeightForWidth(self.label_profile_name.sizePolicy().hasHeightForWidth())
        self.label_profile_name.setSizePolicy(sizePolicy3)
        font10 = QFont()
        font10.setFamilies([u"Montserrat Thin"])
        font10.setPointSize(16)
        font10.setItalic(True)
        font10.setUnderline(True)
        self.label_profile_name.setFont(font10)

        self.horizontalLayout_18.addWidget(self.label_profile_name)


        self.verticalLayout_13.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.frame_20)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        font11 = QFont()
        font11.setFamilies([u"Montserrat SemiBold"])
        font11.setPointSize(16)
        font11.setBold(True)
        self.label_19.setFont(font11)

        self.horizontalLayout_19.addWidget(self.label_19)

        self.label_profile_bought = QLabel(self.frame_20)
        self.label_profile_bought.setObjectName(u"label_profile_bought")
        sizePolicy3.setHeightForWidth(self.label_profile_bought.sizePolicy().hasHeightForWidth())
        self.label_profile_bought.setSizePolicy(sizePolicy3)
        self.label_profile_bought.setFont(font10)

        self.horizontalLayout_19.addWidget(self.label_profile_bought)


        self.verticalLayout_13.addWidget(self.frame_20)


        self.horizontalLayout_16.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setMinimumSize(QSize(600, 0))
        self.frame_15.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_old_pass = QLineEdit(self.frame_18)
        self.lineEdit_old_pass.setObjectName(u"lineEdit_old_pass")
        sizePolicy2.setHeightForWidth(self.lineEdit_old_pass.sizePolicy().hasHeightForWidth())
        self.lineEdit_old_pass.setSizePolicy(sizePolicy2)
        self.lineEdit_old_pass.setMinimumSize(QSize(0, 50))
        self.lineEdit_old_pass.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_old_pass.setFont(font7)
        self.lineEdit_old_pass.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 20px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(85, 170, 255);}")
        self.lineEdit_old_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_17.addWidget(self.lineEdit_old_pass)


        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit_con_new_pass = QLineEdit(self.frame_16)
        self.lineEdit_con_new_pass.setObjectName(u"lineEdit_con_new_pass")
        sizePolicy2.setHeightForWidth(self.lineEdit_con_new_pass.sizePolicy().hasHeightForWidth())
        self.lineEdit_con_new_pass.setSizePolicy(sizePolicy2)
        self.lineEdit_con_new_pass.setMinimumSize(QSize(0, 50))
        self.lineEdit_con_new_pass.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_con_new_pass.setFont(font7)
        self.lineEdit_con_new_pass.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 20px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(85, 170, 255);}")
        self.lineEdit_con_new_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_21.addWidget(self.lineEdit_con_new_pass)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lineEdit_new_pass = QLineEdit(self.frame_17)
        self.lineEdit_new_pass.setObjectName(u"lineEdit_new_pass")
        sizePolicy3.setHeightForWidth(self.lineEdit_new_pass.sizePolicy().hasHeightForWidth())
        self.lineEdit_new_pass.setSizePolicy(sizePolicy3)
        self.lineEdit_new_pass.setMinimumSize(QSize(0, 50))
        self.lineEdit_new_pass.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_new_pass.setFont(font7)
        self.lineEdit_new_pass.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 20px;\n"
"	color: #000000;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(85, 170, 255);}")
        self.lineEdit_new_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_20.addWidget(self.lineEdit_new_pass)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.btn_profile_change = QPushButton(self.frame_21)
        self.btn_profile_change.setObjectName(u"btn_profile_change")
        sizePolicy3.setHeightForWidth(self.btn_profile_change.sizePolicy().hasHeightForWidth())
        self.btn_profile_change.setSizePolicy(sizePolicy3)
        self.btn_profile_change.setMinimumSize(QSize(250, 0))
        self.btn_profile_change.setFont(font5)
        self.btn_profile_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_profile_change.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 60px;\n"
"	padding-right: 60px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: rgb(244, 104, 104);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.btn_profile_change)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.horizontalLayout_16.addWidget(self.frame_15)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_22 = QFrame(self.profile_page)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_9)

        self.btn_logout = QPushButton(self.frame_22)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(350, 0))
        self.btn_logout.setFont(font5)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding-left: 60px;\n"
"	padding-right: 60px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: rgb(244, 104, 104);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 3px solid rgb(48, 50, 62);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"")
        self.btn_logout.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.btn_logout)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)


        self.verticalLayout_9.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.profile_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.center_main_items)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_filter.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_search.setText("")
        self.btn_basket.setText("")
        self.btn_profile.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_image_to_buy.setText("")
        self.label_info_price.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_win.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_proc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_mb.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_video.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_ozu.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_ssd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_hdd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_block.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_cp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_info_cc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_info_buy.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Brands", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Processor ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Operating System", None))
        self.lineEdit_filter_from.setText("")
        self.lineEdit_filter_from.setPlaceholderText(QCoreApplication.translate("MainWindow", u"from", None))
        self.lineEdit_filter_before.setText("")
        self.lineEdit_filter_before.setPlaceholderText(QCoreApplication.translate("MainWindow", u"before", None))
        self.btn_filter_search.setText(QCoreApplication.translate("MainWindow", u"Searsh!", None))
        self.btn_basket_all_clear.setText(QCoreApplication.translate("MainWindow", u"All Clear", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Your Name", None))
        self.label_profile_name.setText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"You bought", None))
        self.label_profile_bought.setText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.lineEdit_old_pass.setText("")
        self.lineEdit_old_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.lineEdit_con_new_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.lineEdit_new_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm New Password ", None))
        self.btn_profile_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Log out!", None))
    # retranslateUi

