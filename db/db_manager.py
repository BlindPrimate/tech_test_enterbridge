import sqlite3


class DBManager:
    """
    DB connection object to manage date entry and retrieval

    Attributes:
        path (str) : path to database
    """
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.conn = self.db.cursor()

    def __del__(self):
        self.db.close()

    def insert_book(self, value_tuple):
        '''Insert book into database.'''
        query = '''
        INSERT INTO books (title, isbn_13, publisher, publication_date, 
                        series, edition_description, pages, sales_rank, 
                        price, product_width, product_height, product_depth) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        '''

        self.conn.execute(query, value_tuple)
        self.db.commit()