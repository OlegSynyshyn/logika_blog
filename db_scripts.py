import sqlite3
class DBManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None

    def open_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
       
    
    def get_categories(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM categories''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_articles(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data

    def get_articles_by_category(self, category_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles articles WHERE category_id=?''', [category_id])
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    

    def get_article_by_id(self, article_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles WHERE id=?''', [article_id])
        data = self.cursor.fetchone()
        self.conn.close()
        return data