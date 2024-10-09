from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
from pathlib import Path
import os

os.chdir(Path(__file__).parent)

# file_ui_login = Path(__file__).parent / "Login.ui"
# file_ui_register = Path(__file__).parent / "Register.ui"

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("Login.ui", self) # load ui
    
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Register.ui", self) # load ui
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_login = Login()
    # window_register = Register()
    window_login.show()
    # window_register.show()
    app.exec()