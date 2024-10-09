from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys, os

from pathlib import Path
os.chdir(Path(__file__).parent)

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Login.ui", self)

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Register.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows_login = Login()
    # windows_login.show()
    windows_register = Register()
    # windows_register.show()
    app.exec()