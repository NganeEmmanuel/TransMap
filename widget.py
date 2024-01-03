# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path

from PySide6.QtCore import QFile, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

from Database import dbInit
from Service import loginService


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        dbInit.create_tables()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        # Access the QPushButton using its object name
        self.loginBtn = self.findChild(QPushButton, "loginBtn")
        self.username = self.findChild(QLineEdit, "username")
        self.password = self.findChild(QLineEdit, "password")
        # Connect the clicked signal of the button to a function
        self.loginBtn.clicked.connect(self.login)

    @Slot()
    def login(self):
        username = self.username.text()
        password = self.password.text()

        # This function will be called when the button is clicked
        loginService.login(username, password)

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.setFixedHeight(471)
    widget.setFixedWidth(761)
    widget.show()
    sys.exit(app.exec_())
