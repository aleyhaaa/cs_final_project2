import sqlite3 # Import SQLite3

"""
This file will control all aspects of communicating with the SQLite3 database

This python program will use the built in SQLite3 module
"""

# CONSTANTS
DATABASE_FILE = "books.sqlite3"

# Initialize a database - SQLite3
con = sqlite3.connect(DATABASE_FILE)

# Create a cursor
cur = con.cursor()

# Create book table

def create_book_table():
    """
    This function will create a book table based off of the following

    - books
        - pid (primary id) - a unique number
        - title:TEXT
        - author_id:INTEGER
        - read_book:BOOLEAN
        - comments:TEXT
        - isbn:TEXT
    """
    sql_statement = """
    CREATE TABLE IF NOT EXISTS books(pid INTEGER NOT NULL PRIMARY KEY, 
    title TEXT, 
    author TEXT,
    read_book BOOLEAN,
    comment TEXT,
    isbn TEXT
    )
    """
    cur.execute(sql_statement)
    return "Database 'books' table created"
    
# Create an author table
def create_author_table():
    """
    This function will create an author table based off of the following 

    - author
        - pid
        - first_name:TEXT
        - last_name:TEXT
    """
    sql_statement = """
    CREATE TABLE IF NOT EXISTS authors(pid INTEGER NOT NULL PRIMARY KEY, 
    first_name TEXT,
    last_name TEXT
    )
    """
    cur.execute(sql_statement)
    return "Database 'authors' table created"

def create_fake_data():
    """
    TODO: fix relational issues
    generate initial fake data to insert in database
    """
    # create authors
  #  cur.execute("INSERT INTO author (first_name, last_name) VALUES ('Aleyha' 'Author')")
  #   cur.execute("INSERT INTO author (first_name, last_name) VALUES ('Michael', 'Author')")

    # Create Books 
    cur.execute("INSERT INTO books (title, author, comment, isbn) VALUES ('Book 1', 'Aleyha', 'interesting book', '12345')") 
    cur.execute("INSERT INTO books (title, author, comment, isbn) VALUES ('Book 2', 'Michael', 'interesting book', '54321')") 
    con.commit() # commits info to database

if __name__ == "__main__":
    create_book_table()
    create_author_table()
    create_fake_data()