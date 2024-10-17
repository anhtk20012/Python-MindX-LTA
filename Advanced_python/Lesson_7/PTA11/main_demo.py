from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import uic
import sys, os

from pathlib import Path
os.chdir(Path(__file__).parent)

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login App")
        button = QPushButton("Press me")
        self.setCentralWidget(button)
        
        button.setCheckable(True)
        button.clicked.connect(self.show_me)
    
    def show_me(self):
        mb_warning = QMessageBox()
        mb_warning.setWindowTitle("Warning")
        mb_warning.setIcon(QMessageBox.Icon.Warning)
        mb_warning.setText("Check username and password")
        mb_warning.setStyleSheet("color: red")
        mb_warning.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows_login = Login()
    windows_login.show()
    app.exec()