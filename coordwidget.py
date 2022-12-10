from PySide6 import QtGui
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal
import sqlite3
from groupaya import Ui_CoordWidget


class CoordWidget(QWidget):
    delete = Signal(int)
    s = 0

    def __init__(self, id_widget: int, parent=None):

        super(CoordWidget, self).__init__(parent)
        self.ui = Ui_CoordWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        try:
            sqliteConnection = sqlite3.connect('all_products.db')
            cursor = sqliteConnection.cursor()
            # print("Connected to SQLite")

            sqlite_select_query = """SELECT * from pc"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            self.ui.label_filter_name.setText(records[CoordWidget.s][1])
            self.ui.label_filter_price.setText(records[CoordWidget.s][12])
            self.image = records[CoordWidget.s][13]
            self.ui.image_product.setPixmap(QtGui.QPixmap(self.image))
            CoordWidget.s += 1
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                # print("The SQLite connection is closed")





