import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Login import LoginWindow as login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = login()
    main_win.show()
    app.exec()