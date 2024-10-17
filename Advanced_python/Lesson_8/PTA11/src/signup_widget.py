import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class SignUp(QMainWindow):
    def __init__(self, signal):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Sign_Up.ui', self)
        self.old_pos = None
        self.signal = signal
        self.ui.pushButton.clicked.connect(self.verify_register)
        self.ui.pushButton_3.clicked.connect(self.close_application)
        self.ui.pushButton_4.clicked.connect(self.show_wellcome)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None
            
    def close_application(self):
        reply = QMessageBox.question(
                    self, 'Exit', 'Are you sure you want to exit?', 
                    QMessageBox.StandardButton.Yes | 
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
                )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def verify_register(self):
        QMessageBox.information(self, 'Registration Success', 'You have successfully registered!', QMessageBox.StandardButton.Yes)
        
    def show_wellcome(self):
        self.signal.wellcome_show.emit(self.pos())
        self.close()
        
    def open_register(self, position):
        self.move(position)
        self.show()