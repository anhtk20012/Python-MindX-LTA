from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys
from random import choice

window_titles = ["Football", "Apple", "Basketball", "Exit"]

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Football")
        
        self.setFixedSize(QSize(400,100))
        
        self.button = QPushButton("Click me")
        
        self.setCentralWidget(self.button)
        
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(self.the_window_title_changed)

    def the_button_was_clicked(self):
        new_window_title = choice(window_titles)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        if window_title == "Exit":
            self.button.setDisabled(True)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()