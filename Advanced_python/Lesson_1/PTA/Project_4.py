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
        self.center_x = (self.width() - 100)/2
        self.center_y = (self.height() - 30)/2
        self.button.move(QPoint(int(self.center_x), int(self.center_y)))
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.button.setFixedSize(QSize(200, 30))
        self.button.move(QPoint(int(self.center_x)- 50, int(self.center_y)))
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        
        self.setWindowTitle("My Oneshot App")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()