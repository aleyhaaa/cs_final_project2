# utility.py
import sqlite3  # SQLite3 module for database management

# Database file name (SQLite database will be created in the same directory)
DATABASE_FILE = "books.sqlite3"

def create_database():
    """
    Create the 'books' table in the SQLite database.
    If the table already exists, it will not be recreated.

    Columns:
    - id: Unique identifier for each book (Primary Key, Auto-incremented).
    - title: The title of the book (Text).
    - author: The author of the book (Text).
    - isbn: The ISBN number of the book (Text).
    - read_book: Boolean indicating if the book has been read (0 = No, 1 = Yes).
    - comment: A text field for any user comments about the book.
    """
    # Establish a connection to the SQLite database
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()  # Create a cursor object for executing SQL commands
        
        # SQL command to create the books table (if it does not already exist)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique book ID (auto-incremented)
            title TEXT,                           -- Book title
            author TEXT,                          -- Book author
            isbn TEXT,                            -- Book ISBN number
            read_book BOOLEAN,                    -- Read status (0 = No, 1 = Yes)
            comment TEXT                          -- User comments about the book
        )
        """)
        
        # Commit the transaction (save changes)
        con.commit()


def read_all_books():
    """
    Read all book records from the 'books' table.

    Returns:
    - A list of tuples, each representing a row in the 'books' table.
    - Each tuple contains (id, title, author, isbn, read_book, comment).
    """
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()  # Create a cursor object
        
        # SQL command to fetch all rows from the books table
        cur.execute("SELECT * FROM books")
        
        # Fetch all results and return as a list of tuples
        return cur.fetchall()


def add_book(title, author, isbn, read_book, comment):
    """
    Add a new book record to the 'books' table.

    Parameters:
    - title (str): The title of the book.
    - author (str): The author of the book.
    - isbn (str): The ISBN number of the book.
    - read_book (bool): Whether the book has been read (True = Read, False = Not Read).
    - comment (str): User comments about the book.
    """
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()  # Create a cursor object
        
        # SQL command to insert a new book record
        cur.execute("""
        INSERT INTO books (title, author, isbn, read_book, comment)
        VALUES (?, ?, ?, ?, ?)
        """, (title, author, isbn, read_book, comment))
        
        # Commit the transaction (save changes)
        con.commit()


def update_book(book_id, title, author, isbn, read_book, comment):
    """
    Update an existing book record in the 'books' table.

    Parameters:
    - book_id (int): The unique ID of the book to update.
    - title (str): The updated title of the book.
    - author (str): The updated author of the book.
    - isbn (str): The updated ISBN number of the book.
    - read_book (bool): The updated read status (True = Read, False = Not Read).
    - comment (str): The updated user comments about the book.
    """
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()  # Create a cursor object
        
        # SQL command to update a book record
        cur.execute("""
        UPDATE books 
        SET title = ?, author = ?, isbn = ?, read_book = ?, comment = ?
        WHERE id = ?
        """, (title, author, isbn, read_book, comment, book_id))
        
        # Commit the transaction (save changes)
        con.commit()


def delete_book(book_id):
    """
    Delete a book record from the 'books' table.

    Parameters:
    - book_id (int): The unique ID of the book to delete.
    """
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()  # Create a cursor object
        
        # SQL command to delete a book record based on the book ID
        cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        
        # Commit the transaction (save changes)
        con.commit()