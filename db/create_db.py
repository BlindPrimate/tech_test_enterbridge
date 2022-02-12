import sqlite3

conn = sqlite3.connect('./sqllitedb')
c = conn.cursor()

c.execute(
    '''
        CREATE TABLE IF NOT EXISTS books
        (id INTEGER PRIMARY KEY, 
        title text, 
        isbn_13 integer,
        publisher text,
        publication_date text,
        series text,
        edition_description text,
        pages text,
        sales_rank text,
        price real,
        product_width real,
        product_height real,
        product_depth real
        )
    '''
)


conn.commit()
