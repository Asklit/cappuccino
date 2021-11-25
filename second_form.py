import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

NAME_DATABASE = "coffee.sqlite"


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.btn_add.clicked.connect(self.add_to_db)
        self.btn_save.clicked.connect(self.save_in_db)
        self.fill_table_widget()

    def fill_table_widget(self):
        con = sqlite3.connect(NAME_DATABASE)
        cur = con.cursor()
        self.result = cur.execute(f"""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()

    def add_to_db(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

    def save_in_db(self):
        con = sqlite3.connect(NAME_DATABASE)
        cur = con.cursor()
        cur.execute(f"""DELETE FROM coffee""").fetchall()
        con.commit()
        res = []
        for i in range(self.tableWidget.rowCount()):
            res2 = []
            for j in range(self.tableWidget.columnCount()):
                try:
                    if j == 0:
                        res2.append(int(self.tableWidget.item(i, j).text()))
                    else:
                        res2.append(self.tableWidget.item(i, j).text())
                    if self.tableWidget.item(i, j).text() == "":
                        raise AttributeError
                except AttributeError:
                    self.status_bar.setText("Введите корректные данные")
            res.append(res2)
        for i, j, k, l, g, d, h in res:
            con = sqlite3.connect(NAME_DATABASE)
            cur = con.cursor()
            cur.execute(
                f"""INSERT INTO coffee('name of the variety','degree of roasting','ground/in grains',
                'taste description','price','packing volume') VALUES(
                '{j}', '{k}', '{l}', '{g}', '{d}', '{h}')""").fetchall()
            con.commit()
