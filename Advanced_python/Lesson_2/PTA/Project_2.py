from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Application")
        self.setFixedSize(QSize(400,200))
    
    def mouseMoveEvent(self, e):
        print("Mouse move")
        
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print("Press Left")
        if e.button() == Qt.MouseButton.MiddleButton:
            print("Press Middle")
        if e.button() == Qt.MouseButton.RightButton:
            print("Press Right")
            
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print("Release Left")
        if e.button() == Qt.MouseButton.MiddleButton:
            print("Release Middle")
        if e.button() == Qt.MouseButton.RightButton:
            print("Release Right")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print("Double Left")
        if e.button() == Qt.MouseButton.MiddleButton:
            print("Double Middle")
        if e.button() == Qt.MouseButton.RightButton:
            print("Double Right")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()