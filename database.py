# database.py
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import os

def create_connection():
    
    db_path = os.path.join(os.path.dirname(__file__), 'students.db')
    
    
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_path)
    
    
    if not db.open():
        print("Не удалось открыть базу данных!")
        return None
    
    print("База данных успешно открыта!")
    return db

def init_db():
    
    query = QSqlQuery()

    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор студента
        name TEXT NOT NULL,                    -- Имя студента
        grade TEXT NOT NULL                    -- Оценка студента
    );
    '''
    
    
    if not query.exec_(create_table_query):
        print("Ошибка при создании таблицы:", query.lastError().text())
    else:
        print("Таблица students2 успешно создана или уже существует!")
