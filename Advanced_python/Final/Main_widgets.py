from PyQt6.QtWidgets import QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QPixmap
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(Path(__file__).parent / "main_windows.ui", self)
        self.initUI()
        
    def initUI(self):
        dir = Path(__file__).parent
        self.setWindowTitle('Main Application')
        self.setFixedSize(QSize(960,540))
        
        self.ui.label.setText("")
        pixmap = QPixmap(str(dir/'image/icons-clinic.png'))
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)
        
        self.ui.label_2.setText("")
        pixmap_2 = QPixmap(str(dir/'image/icons-cart.png'))
        self.ui.label_2.setPixmap(pixmap_2)
        self.ui.label_2.setScaledContents(True)
        
        self.ui.label_3.setText("")
        pixmap_3 = QPixmap(str(dir/'image/icons-settings.png'))
        self.ui.label_3.setPixmap(pixmap_3)
        self.ui.label_3.setScaledContents(True)
        
        self.ui.pushButton.setText("")
        self.ui.label_6.setText("")
        pixmap_4 = QPixmap(str(dir/'image/icons-search.png'))
        self.ui.label_4.setPixmap(pixmap_4)
        self.ui.label_4.setScaledContents(True)
                
    def on_login_successful(self):
        self.show()

from PyQt6.QtWidgets import QApplication
import sys               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_windown = MainWindow()
    main_windown.show()
    app.exec()