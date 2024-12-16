# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow
from database import create_connection, init_db

if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    db = create_connection()
    if db:
        init_db()  

    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
