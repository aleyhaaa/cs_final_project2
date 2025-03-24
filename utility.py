# Initialize a database - SQlite3

# CRUD (Create, Read, Update, Delete)

def create_book(title:str, isbn:str, author_id:int, read_book:bool=False, comment:str=None):
    """
    This function is used to create a record of a book
    """
    pass

def create_author(first_name:str, last_name:str):
    """
    This will create a record for the author
    """
    pass

def read_book_record(isbn:str):
    """
    Retrive data from the database
    """
    pass

def read_all_books():
    """
    Read all the books in the database
    """
    pass

def update_book(isbn:str):
    """
    Update fields in a book record
    """
    pass

def delete_book(isbn:str):
    """
    This function will delete a book based off of the ISBN
    """
    pass

# Export all books in the database to CSV

def export_report():
    """
    This function will output database to a CSV file
    """
    pass