import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QSize, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Thiết lập đối tượng đầu tiên
        self.setWindowTitle('Project 1') # Thiết lập tên ứng dụng
        self.setFixedSize(QSize(400, 300)) # Thiết lập kích thước
        
        widget = QWidget(self) # tạo container
        self.setCentralWidget(widget) # Thêm container vào cửa sổ

        button = QPushButton('Connect', widget) # Tạo button trong container
        button.setFixedSize(QSize(100, 30))
        center_x = (self.width() - 100)/2
        center_y = (self.height() - 30)/2
        button.move(QPoint(int(center_x), int(center_y)))
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()