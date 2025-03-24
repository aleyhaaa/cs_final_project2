import sqlite3 # Import SQLite3

"""
This file will control all aspects of communicating with the SQLite3 database
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
        - title:str
        - author_id:int
        - read_book:bool
        - comments:str
        - isbn:str

    """
    pass
# Create an author table
def create_author_table():
    """
    This function will create an author table based off of the following 
    - author
        - pid
        - first_name:str
        - last_name:str
    """
    pass