import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtCore import QSize, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Project 3')
        self.setFixedSize(QSize(400, 300))
        
        widget = QWidget(self)
        self.setCentralWidget(widget)

        self.button = QPushButton('Connect', widget)
        self.button.setFixedSize(QSize(100, 30))
        center_x = (self.width() - 100)/2
        center_y = (self.height() - 30)/2
        self.button.move(QPoint(int(center_x), int(center_y)))

        self.button_is_checked = True
        self.button.setCheckable(True)
        
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()