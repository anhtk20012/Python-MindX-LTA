from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Application")
        self.setFixedSize(QSize(400,200))
        
        self.label = QLabel()
        self.label1 = QLabel()
        self.input = QLineEdit()
        self.button = QPushButton("Click me")
        layout = QVBoxLayout()
        
        layout.addWidget(self.input)
        self.input.textChanged.connect(self.label1.setText)
        
        layout.addWidget(self.button)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.input.returnPressed.connect(self.the_button_was_clicked)
        
        layout.addWidget(self.label)
        
        layout.addWidget(self.label1)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
    def the_button_was_clicked(self):
        text = self.input.text()
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()