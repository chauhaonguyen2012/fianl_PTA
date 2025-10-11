from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic 
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
    sys

