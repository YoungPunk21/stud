# ui_main.py
from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from students_model import StudentsModel
from database import create_connection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список студентов")
        self.setGeometry(100, 100, 600, 400)

        
        self.db = create_connection()
        if not self.db:
            return

        
        self.model = StudentsModel(db=self.db)

        
        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)

        self.add_button = QPushButton("Добавить студента", self)
        self.add_button.clicked.connect(self.add_student)

        self.delete_button = QPushButton("Удалить студента", self)
        self.delete_button.clicked.connect(self.delete_student)

        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def add_student(self):
        name = "Новое имя"  
        grade = "5"         

        query = QSqlQuery()
        query.prepare("INSERT INTO students2 (name, grade) VALUES (?, ?)")
        query.addBindValue(name)
        query.addBindValue(grade)
        query.exec_()
        
        
        self.model.select()

    def delete_student(self):
        
        selected_indexes = self.table_view.selectedIndexes()
        if selected_indexes:
            
            student_id = self.model.data(selected_indexes[0], role=0)  
            print(f"Удаляем студента с ID: {student_id}")

            
            query = QSqlQuery()
            query.prepare("DELETE FROM students2 WHERE id = ?")
            query.addBindValue(student_id)
            if query.exec_():
                print("Студент удален")
                self.model.select()  
            else:
                print("Ошибка при удалении студента:", query.lastError().text())
