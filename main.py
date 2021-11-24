import sqlite3
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

NAME_DATABASE = "coffee.sqlite"


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_file.ui', self)
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QApplication(sys.argv)
# app.setStyle('Fusion')
ex = MyWidget()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())