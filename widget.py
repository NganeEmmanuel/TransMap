# This Python file uses the following encoding: utf-8
import datetime
import os
import sys
from pathlib import Path

from PySide6.QtCore import QFile, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QStackedWidget, QVBoxLayout

from Database import dbInit, crud
from Service import loginService
from model.user import User


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
        self.formWidget = loader.load(ui_file, self)
        ui_file.close()

        # Access the QPushButton using its object name
        self.loginBtn = self.findChild(QPushButton, "loginBtn")
        self.username = self.findChild(QLineEdit, "username")
        self.password = self.findChild(QLineEdit, "password")
        self.errormsg = self.findChild(QLabel, "errormsg")
        # Connect the clicked signal of the button to a function
        self.loginBtn.clicked.connect(self.login)

        # Create a User object
        # user = User()
        #
        # # Set values to its attributes
        # user.username = "john"
        # user.password = "password123"
        # user.email = "john@example.com"
        # # ... set values for other attributes
        #
        # # Set the date joined and updated date attributes
        # user.date_joined = datetime.datetime.now().date()
        # user.updated_date = datetime.datetime.now().date()
        #
        # crud.add(user)

        # Create the dashboard window
        self.dashboardWidget = QWidget()
        dashboardLayout = QVBoxLayout(self.dashboardWidget)
        dashboardLabel = QLabel("Welcome to the Dashboard!")
        dashboardLayout.addWidget(dashboardLabel)

        # Create a stacked widget and add the login form and dashboard window
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.formWidget)
        self.stackedWidget.addWidget(self.dashboardWidget)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.stackedWidget)

    @Slot()
    def login(self):
        username = self.username.text()
        password = self.password.text()

        # This function will be called when the button is clicked
        isLogin = loginService.login(username, password)
        if (isLogin == "success"):
            self.stackedWidget.setCurrentWidget(self.dashboardWidget)
        else:
            self.errormsg.setText(isLogin)


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.setFixedHeight(471)
    widget.setFixedWidth(761)
    widget.show()
    sys.exit(app.exec_())
