import sqlite3

conn = sqlite3.connect('../test_database')
c = conn.cursor()

c.execute(
    '''
        CREATE TABLE IF NOT EXISTS books
        (id INTEGER PRIMARY KEY, 
        name varchar(255), 
        isbn_13 integer,
        publisher text,
        publication_date text,
        series text,
        description text,
        pages text,
        sales_rank text,
        product_width real,
        product_height real,
        product_depth real,
        price real
        )
    '''
)


conn.commit()
