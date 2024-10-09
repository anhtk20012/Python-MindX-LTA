# Thêm thư viện cần thiết
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Thiết lập thành phần để mở ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()