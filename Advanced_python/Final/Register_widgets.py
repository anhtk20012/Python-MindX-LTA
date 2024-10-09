import sys, re
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QComboBox, QDateEdit, QFrame
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt, QSize, QDate, pyqtSignal
from pathlib import Path

class Register(QMainWindow):
    def __init__(self, signal_manager):
        super().__init__()
        self.initUI()
        
        self.signal_manager = signal_manager
    
    def initUI(self):
        dir = Path(__file__).parent
        self.setWindowTitle('Register Application')
        self.setFixedSize(QSize(960,540))
        self.setGeometry(100, 100, 960, 540)
        
        self.setWindowIcon(QIcon(str(dir/'image/logo_shop.png'))) 
        
        background = QPixmap(str(dir/'image/background_signup.png'))
        scaled_background = background.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_background))
        self.setPalette(palette)    
        
        self.fullname_label = QLabel('Full Name:', self)
        self.fullname_input = QLineEdit(self)
        self.fullname_label.setStyleSheet("font-weight: bold;")
        
        self.dob_label = QLabel('Date of Birth:', self)
        self.dob_input = QDateEdit(self)
        self.dob_input.setCalendarPopup(True)
        self.dob_input.setDisplayFormat('dd/MM/yyyy')
        self.dob_input.setDate(QDate(1990,12,1)) # QDate.currentDate()
        
        self.dob_label.setStyleSheet("font-weight: bold;")

        self.gender_label = QLabel('Gender:', self)
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(['Male', 'Female', 'Other'])
        self.gender_label.setStyleSheet("font-weight: bold;")
        
        self.username_label = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.username_label.setStyleSheet("font-weight: bold;")
        
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_label.setStyleSheet("font-weight: bold;")
        
        self.confirm_password_label = QLabel('Confirm Password:', self)
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_label.setStyleSheet("font-weight: bold;")

        self.register_button = QPushButton('Register', self)
        self.register_button.clicked.connect(self.register_user)
        
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.show_login)
        
        input_width = 200
        self.fullname_input.setFixedWidth(input_width)
        self.dob_input.setFixedWidth(input_width)
        self.gender_input.setFixedWidth(input_width)
        self.username_input.setFixedWidth(input_width)
        self.password_input.setFixedWidth(input_width)
        self.confirm_password_input.setFixedWidth(input_width)

        vbox = QVBoxLayout()

        input_fullname = QHBoxLayout()
        input_fullname.addWidget(self.fullname_label)
        input_fullname.addWidget(self.fullname_input)

        input_dob = QHBoxLayout()
        input_dob.addWidget(self.dob_label)
        input_dob.addWidget(self.dob_input)

        input_gender = QHBoxLayout()
        input_gender.addWidget(self.gender_label)
        input_gender.addWidget(self.gender_input)

        input_username = QHBoxLayout()
        input_username.addWidget(self.username_label)
        input_username.addWidget(self.username_input)

        input_password = QHBoxLayout()
        input_password.addWidget(self.password_label)
        input_password.addWidget(self.password_input)

        input_confirm_password = QHBoxLayout()
        input_confirm_password.addWidget(self.confirm_password_label)
        input_confirm_password.addWidget(self.confirm_password_input)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.register_button)
        btn_layout.addWidget(self.login_button)

        vbox.addLayout(input_fullname)
        vbox.addLayout(input_dob)
        vbox.addLayout(input_gender)
        vbox.addLayout(input_username)
        vbox.addLayout(input_password)
        vbox.addLayout(input_confirm_password)
        vbox.addLayout(btn_layout)

        container = QWidget(self)
        container.setGeometry(520, 200, 350, 300)
        container.setLayout(vbox)

        container_background = QFrame(self)
        container_background.setStyleSheet("background-color: rgba(255, 255, 255, 240); border-radius: 10px;")
        container_background.setGeometry(container.geometry())
        
        container.raise_()
    
    def register_user(self):
        fullname = self.fullname_input.text()
        dob = self.dob_input.date().toString('yyyy-MM-dd')
        gender = self.gender_input.currentText()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        if not self.is_valid_username(username):
            self.show_message('Error', 'Username must be 3-15 characters long, contain only letters, numbers, dots, or underscores, and cannot start or end with a special character.')
            return
        
        if not self.is_valid_password(password, username):
            self.show_message('Error', 'Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.')
            return
        
        if password != confirm_password:
            self.show_message('Error', 'Passwords do not match')
            return

        if not all([fullname, dob, gender, username, password, confirm_password]):
            self.show_message('Error', 'All fields are required')
            return

        if self.save_credentials(fullname, dob, gender, username, password):
            self.show_message('Success', 'Registration successful!')
            self.clear_inputs()
        else:
            self.show_message('Error', 'Username already exists')
            return
            
        self.emit_register_signal()
        self.close()

    def is_valid_username(self, username):
        if not 3 <= len(username) <= 15:
            return False
        if not re.match("^[a-zA-Z0-9._]+$", username):
            return False
        if username[0] in '._' or username[-1] in '._':
            return False
        return True

    def is_valid_password(self, password, username):
        if len(password) < 8:
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        if username.lower() in password.lower():
            return False
        return True
    
    def save_credentials(self, fullname, dob, gender, username, password):
        dir = Path(__file__).parent
        credentials_path = dir / 'credentials.txt'

        if not credentials_path.exists():
            credentials_path.touch()

        with open(credentials_path, 'r', encoding='utf-8') as file:
            for line in file:
                existing_username, _ = line.strip().split(',')[3:5]
                if existing_username == username:
                    return False

        with open(credentials_path, 'a', encoding='utf-8') as file:
            file.write(f'{fullname},{dob},{gender},{username},{password}\n')
        return True

    def clear_inputs(self):
        self.fullname_input.clear()
        self.dob_input.setDate(QDate(1990,12,1))
        self.gender_input.setCurrentIndex(0)
        self.username_input.clear()
        self.password_input.clear()
        self.confirm_password_input.clear()
        
    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information if title == 'Success' else QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
    
    def show_login(self):
        self.signal_manager.show_login_signal.emit()
        self.close()
    
    def emit_register_signal(self):
        self.signal_manager.register_true.emit()