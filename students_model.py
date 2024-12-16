# students_model.py
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt

class StudentsModel(QSqlTableModel):
    def __init__(self, parent=None, db=None):
        super().__init__(parent, db)
        self.setTable('students2')
        self.select()  
        self.setEditStrategy(QSqlTableModel.OnFieldChange)  
        self.setHeaderData(1, Qt.Horizontal, "Имя")  
        self.setHeaderData(2, Qt.Horizontal, "Оценка")  
