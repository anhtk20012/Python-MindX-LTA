import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QFrame
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from pathlib import Path

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        dir = Path(__file__).parent
        self.setWindowTitle('Login Application')
        self.setFixedSize(QSize(960,540))
        self.setGeometry(100, 100, 960, 540)
        
        self.setWindowIcon(QIcon(str(dir/'image/logo_shop.png'))) 
        
        background = QPixmap(str(dir/'image/background.png'))
        scaled_background = background.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_background))
        self.setPalette(palette)

        self.username_label = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.username_label.setStyleSheet("font-weight: bold;")
        
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_label.setStyleSheet("font-weight: bold;")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.check_login)

        self.signup_button = QPushButton('Sign Up', self)
        self.signup_button.clicked.connect(self.open_signup)
        
        input_width = 300
        self.username_input.setFixedWidth(input_width)
        self.password_input.setFixedWidth(input_width)
        
        vbox = QVBoxLayout()

        input_username = QHBoxLayout()
        input_username.addWidget(self.username_label)
        input_username.addWidget(self.username_input)

        input_password = QHBoxLayout()
        input_password.addWidget(self.password_label)
        input_password.addWidget(self.password_input)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.login_button)
        btn_layout.addWidget(self.signup_button)
        
        vbox.addLayout(input_username)
        vbox.addLayout(input_password)
        vbox.addLayout(btn_layout)
        
        container = QWidget(self)
        container.setGeometry(520, 300, 390, 200)
        container.setLayout(vbox)

        container_background = QFrame(self)
        container_background.setStyleSheet("background-color: rgba(255, 255, 255, 240); border-radius: 10px;")
        container_background.setGeometry(container.geometry())
        
        container.raise_()
    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.verify_credentials(username, password):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle('Success')
            msg_box.setText('Login successful!')
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle('Error')
            msg_box.setText('Bad username or password')
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
    
    def verify_credentials(self, username_input, password_input):
        dir = Path(__file__).parent
        with open(dir / 'credentials.txt', 'r', encoding='utf-8') as file:
            for line in file:
                username, password = line.strip().split(',')[3:5]
                if username == username_input and password == password_input:
                    return True
        return False      

    def open_signup(self):
        self.close()
        self.open_signup_signal.emit()