import sys, os
from PyQt6 import uic, QtCore
from src import wellcome_widget, signin_widget, signup_widget
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    wellcome_show = QtCore.pyqtSignal(QtCore.QPoint)
    login_show = QtCore.pyqtSignal(QtCore.QPoint)
    register_show = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):   
    def __init__(self):
        self.signal = Signal()
        self.wellcome = wellcome_widget.Wellcome(self.signal)
        self.signin = signin_widget.SignIn(self.signal)
        self.signup = signup_widget.SignUp(self.signal)
        
        self.signal.wellcome_show.connect(self.wellcome.open_wellcome)
        self.signal.login_show.connect(self.signin.open_login)
        self.signal.register_show.connect(self.signup.open_register)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.wellcome.show()
    app.exec()