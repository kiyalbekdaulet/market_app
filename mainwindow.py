import sqlite3

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from one import Ui_MainWindow
from coordwidget import CoordWidget




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0
        # self.ui.btn_search.clicked.connect(self.add_coordwidget)
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.all_products_page))
        self.ui.btn_filter.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.filter_page))
        self.ui.btn_profile.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile_page))
        self.ui.btn_basket.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.basket_page))
        # self.ui.btn_filter_search.clicked.connect(lambda: self.filter())
        self.ui.btn_logout.clicked.connect(lambda: self.close())
        self.ui.btn_profile_change.clicked.connect(lambda: self.ChangePass())
        # self.ui.btn_search.clicked.connect(lambda: self.Search())

        try:
            sqliteConnection = sqlite3.connect('all_products.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_select_query = """SELECT * from pc"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            self.a = len(records)
            for i in range(self.a):
                self.add_coordwidget()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        self.All_Change()
    def ChangePass(self):
        self.con = sqlite3.connect("users.db")
        self.cur = self.con.cursor()
        self.name = self.ui.label_profile_name.text()
        self.password = self.ui.lineEdit_old_pass.text()
        self.new = self.ui.lineEdit_new_pass.text()
        if self.password == self.new:
            print("Error")
        else:
            self.cur.execute("""UPDATE clients SET password  = ? where name = ?""", (self.new,self.name,))
            self.con.commit()
            self.con.close()

    def All_Change(self):
        #Name
            self.sqliteConnection = sqlite3.connect('change_product.db')
            self.cursor = self.sqliteConnection.cursor()
            self.cursor.execute("""SELECT name FROM ozu""")
            self.all_name = self.cursor.fetchall()
            for i in self.all_name:
                    self.ui.comboBox_filter_ram.addItem(i[0])
        #WIN
            self.sqliteConnection = sqlite3.connect('change_product.db')
            self.cursor = self.sqliteConnection.cursor()
            self.cursor.execute("""SELECT name FROM win""")
            self.all_win = self.cursor.fetchall()
            for i in self.all_win:
                    self.ui.comboBox_filter_win.addItem(i[0])
        #Proc
            self.sqliteConnection = sqlite3.connect('change_product.db')
            self.cursor = self.sqliteConnection.cursor()
            self.cursor.execute("""SELECT name FROM proc""")
            self.all_proc = self.cursor.fetchall()
            for i in self.all_proc:
                    self.ui.comboBox_filter_proc.addItem(i[0])
        #MB
            self.sqliteConnection = sqlite3.connect('change_product.db')
            self.cursor = self.sqliteConnection.cursor()
            self.cursor.execute("""SELECT name FROM name""")
            self.all_mb = self.cursor.fetchall()
            for i in self.all_mb:
                    self.ui.comboBox_filter_brand.addItem(i[0])
    def filter(self):
        fr = self.ui.lineEdit_filter_from.text()
        before = self.ui.lineEdit_filter_before.text()
        win = self.ui.comboBox_filter_win.currentText()
        proc = self.ui.comboBox_filter_proc.currentText()
        name = self.ui.comboBox_filter_brand.currentText()
        ozu = self.ui.comboBox_filter_ram.currentText()

        if len(fr) == 0 and len(before) == 0:
            print("Error")
        else:
            try:
                sqliteConnection = sqlite3.connect('all_products.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_select_query = """SELECT * from pc"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                self.a = len(records)
                for i in range(self.a):
                    if records[i][12] > fr and records[i][12] < before or name == records[i][1] or win == records[i][2] or proc == records[i][3] or ozu == records[i][6]:
                        self.add_coordwidget()
                        self.ui.btn_search.clicked.connect(
                            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.all_products_page))

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
    def Search(self):
        # self.need = self.ui.lineEdit_search.text()
        # try:
        #     sqliteConnection = sqlite3.connect('all_products.db')
        #     cursor = sqliteConnection.cursor()
        #     print("Connected to SQLite")
        #     sqlite_select_query = """SELECT * from pc"""
        #     cursor.execute(sqlite_select_query)
        #     self.clear_area()
        for i in range(2):
            self.add_coordwidget(i)

        # except sqlite3.Error as error:
        #     print("Failed to read data from sqlite table", error)
        # finally:
        #     if sqliteConnection:
        #         sqliteConnection.close()
        #         print("The SQLite connection is closed")
    @Slot()
    def add_coordwidget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id)
        self.ui.add_all_product.addWidget(coord_widget)
        # coord_widget.delete.connect(self.delete_coordwidget)

    @Slot()
    def add(self,i):
        self.counter_id += 1
        coord_widget = CoordWidget(i)
        self.ui.basket_all_product.addWidget(coord_widget)
        # coord_widget.delete.connect(self.delete_coordwidget)
    @Slot()
    def clear_area(self):
        while self.ui.add_all_product.count() > 0:
            item = self.ui.add_all_product.takeAt(0)
            item.widget().deleteLater()

    # @Slot(int)
    # def delete_coordwidget(self, wid: int):
    #     print(f'Удаляем виджет с id: {wid}')
    #     widget = self.sender()
    #     self.ui.add_all_product.removeWidget(widget)
    #     widget.deleteLater()

