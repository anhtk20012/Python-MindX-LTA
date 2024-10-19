import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Wellcome(QMainWindow):
    def __init__(self, signal):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Welcome.ui', self)
        self.old_pos = None
        self.signal = signal
        self.ui.label_4.setStyleSheet(
            """
                QLabel {
                    image: url('../resources/images/logo/logo_page1.png');
                }
            """
        )
        self.ui.pushButton.clicked.connect(self.show_login)
        self.ui.pushButton_2.clicked.connect(self.show_register)
        self.ui.pushButton_3.clicked.connect(self.close_application)
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
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close_application()
                          
    def close_application(self):
        reply = QMessageBox.question(
                    self, 'Exit', 'Are you sure you want to exit?', 
                    QMessageBox.StandardButton.Yes | 
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
                )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def show_login(self):
        self.signal.login_show.emit(self.pos())
        self.close()

    def show_register(self):
        self.signal.register_show.emit(self.pos())
        self.close()
        
    def open_wellcome(self, position):
        self.move(position)
        self.show()