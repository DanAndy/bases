import sqlite3
from vibberidb import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)

def login(login, passw, signal):
    con = sqlite3.connect('handler_bd/aaapopbd')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()
    
    if value != []:
        signal.emit('Успешная авторизация!')
        
        MainWindow.show_window_1()
        
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()


def register(login, passw, signal):
    con = sqlite3.connect('handler_bd/aaapopbd')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')

    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()
