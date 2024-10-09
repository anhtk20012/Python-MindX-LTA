import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtCore import QSize, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Project 2')
        self.setFixedSize(QSize(400, 300))
        
        widget = QWidget(self)
        self.setCentralWidget(widget)

        self.button = QPushButton('Connect', widget)
        self.button.setFixedSize(QSize(100, 30))
        center_x = (self.width() - 100)/2
        center_y = (self.height() - 30)/2
        self.button.move(QPoint(int(center_x), int(center_y))) # Di chuyển tới vị trí cho trước

        self.button_is_checked = False # tạo checked
        self.button.setCheckable(True) # bật checked
        self.button.clicked.connect(self.the_button_was_toggled) # Khi button được bấm sẽ kết nối tới hàm bên trong
        self.button.setChecked(self.button_is_checked) # Thiết lập biến checked bằng giá trị nhận được trong self
        
    def the_button_was_toggled(self, state):
        self.button_is_checked = state
        print(self.button_is_checked)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()