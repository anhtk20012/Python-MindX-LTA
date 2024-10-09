import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import pyqtSignal
from Login_widgets import Login
from Register_widgets import Register
from Main_widgets import MainWindow

class SignalManager(QWidget):
    login_true = pyqtSignal()
    register_true = pyqtSignal()
    show_register_signal = pyqtSignal()
    show_login_signal = pyqtSignal()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    signal_manager = SignalManager()
    
    loginPage = Login(signal_manager)
    registerPage = Register(signal_manager)
    mainPage = MainWindow()
    
    signal_manager.login_true.connect(mainPage.on_login_successful)
    signal_manager.register_true.connect(loginPage.on_register_successful)
    signal_manager.show_register_signal.connect(registerPage.show)
    signal_manager.show_login_signal.connect(loginPage.show)
    
    loginPage.show()
    app.exec()