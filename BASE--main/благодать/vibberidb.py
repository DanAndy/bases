import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
import viborbd
import servicee
import sys
import sqlite3
from check_db import *
from des import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from service import Ui_Form

class MyWidget1(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget1, self).__init__()
        loadUi("handler_bd\\service.ui")
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler_bd\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from 'services'")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from services"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.lename.text(), self.lecode.text(), self.lecount.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, name, code, count)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget2(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget2, self).__init__()
        loadUi("handler_bd\\xexexex.ui")
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler_bd\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from workers")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from workers"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.lepost.text(), self.lename.text(), self.leINN.text(), self.leSNILS.text(), self.lePhone.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, post, name, INN, SNILS, Phone)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget3(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget3, self).__init__()
        loadUi("handler\\client.ui")
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler_bd\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from client")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from client"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(),self.leFIO.text(),self.leCodeClient.text(),self.leSeria.text(),
               self.leNomer.text(),self.leHP.text(),self.lePostIndex.text(),self.leCity.text(),
               self.leStreet.text(),self.leHouse.text(),self.leFlat.text(),self.leLogin.text(),self.lePass.text(),]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, FIO, кодклиента, серия, номер, др, post_index, city, street, house, flat, login, pass)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget4(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget4, self).__init__()
        loadUi("handler_bd\\zakazi.ui")
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler_bd\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from zakazi")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from zakazi"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.leCode.text(), self.leDate.text(), self.leTime.text(), self.leCodeClient.text(), self.leTimeClose.text(), self.leTimeHour.text(), self.leCodeYslygi.text(), self.leHeigh.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into zakazi (ID, Кодзаказа, Датасоздания, Времязаказа, Кодклиента, Датазакрытия, Времявчасах, кодуслуги, старшийсмены)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MainWindow1(QWidget):
    def __init__(self):
        super(MainWindow1, self).__init__()
        loadUi("handler_bd\\viborbd.ui", self)
        # loadUi("handler\\zakazi.ui", self)
        # loadUi("handler\\client.ui", self)
        # loadUi("handler\\service.ui", self)
        # loadUi("handler\\xexexex.ui", self)
        # self.pushButton.clicked.connect(self.gotoService)
        # self.pushButton_2.clicked.connect(self.gotoWorkers)
        # self.pushButton_3.clicked.connect(self.gotoClient)
        # self.pushButton_4.clicked.connect(self.gotoZakazi)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
    #
    def login(self, login, signal):
        con = sqlite3.connect('handler_bd/blagodat.db')
        cur = con.cursor()

        # Проверяем есть ли такой пользователь
        cur.execute(f'SELECT * FROM admin WHERE name="{login}";')
        value = cur.fetchall()
        def show_window_1(self):
            self.w1 = MainWindow1()
            self.w1.pushButton.clicked.connect(self.gotoService)
            self.w1.pushButton.clicked.connect(self.w1.close)
            # self.w1.show()

        # def show_window_1(self):
            # self.w1 = MainWindow1()
            self.w1.pushButton_2.clicked.connect(self.gotoWorkers)
            self.w1.pushButton_2.clicked.connect(self.w1.close)
            # self.w1.show()

        # def show_window_1(self):
            # self.w1 = MainWindow1()
            self.w1.pushButton_3.clicked.connect(self.gotoClient)
            self.w1.pushButton_3.clicked.connect(self.w1.close)
            # self.w1.show()

        # def show_window_1(self):
            # self.w1 = MainWindow1()
            self.w1.pushButton_4.clicked.connect(self.gotoZakazi)
            self.w1.pushButton_4.clicked.connect(self.w1.close)
            self.w1.show()
        if value != []:
            
            signal.emit('Успешная авторизация!')
            show_window_1(MainWindow)
            
            
        else:
            signal.emit('Проверьте правильность ввода данных!')

        cur.close()
        con.close()
    #
    def register(login, passw, signal):
        con = sqlite3.connect('handler_bd/blagodat.db')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM admin WHERE name="{login}";')
        value = cur.fetchall()

        if value != []:
            signal.emit('Такой ник уже используется!')

        elif value == []:
            cur.execute(f"INSERT INTO admin (name, password) VALUES ('{login}', '{passw}')")
            signal.emit('Вы успешно зарегистрированы!')
            con.commit()

        cur.close()
        con.close()
###############################################################################################################################################################################################
  
   

    def gotoService(self):
        MainWindow.w2 = MyWidget1()
        MainWindow.w2.show()
        # loadUi("handler\\service.ui", self)

    def gotoWorkers(self):
        MainWindow.w2 = MyWidget2()
        MainWindow.w2.show()
        # loadUi("handler\\xexexex.ui", self)

    def gotoClient(self):
        MainWindow.w2 = MyWidget3()
        MainWindow.w2.show()
        # loadUi("handler\\client.ui", self)
    
    def gotoZakazi(self):
        MainWindow.w2 = MyWidget4()
        MainWindow.w2.show()
        # loadUi("handler\\zakazi.ui", self)
#####################################################################################################################################################################################################
class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    

    def thr_login(self, name, passw):
        MainWindow.login(name, passw, self.mysignal)

    def thr_register(self, name, passw):
        MainWindow.register(name, passw, self.mysignal)

#########################################################################################################################################################################################################
class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form_reg()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    # Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)


    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)


    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
