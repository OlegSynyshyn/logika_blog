import sqlite3
class DBManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
    
    def get_categories(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT * FROM categories''')
        data = self.cursor.fetchall
        self.conn.close()
        return data