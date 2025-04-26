from database import cur, con
import csv

# CRUD (Create, Read, Update, Delete)

def create_book(title:str, isbn:str, author_id:int, read_book:bool=False, comment:str=None):
    """
    This function is used to create a record of a book
    """
    
    data = (title, isbn, author_id, read_book, comment)
    sql_statement = """
    INSERT INTO books(title, isbn, author_id, read_book, comment) VALUES(?,?,?,?,?)
    """
    cur.execute(sql_statement, data)
    con.commit()
    return 'Data inserted into database'

def create_author(first_name:str, last_name:str):
    """
    This will create a record for the author
    """
    data = (first_name, last_name)
    sql_statement = """
    INSERT INTO authors(first_name, last_name) VALUES(?,?)
    """
    cur.execute(sql_statement, data)
    con.commit()
    return 'Data inserted into database'

def read_book_record(isbn:str):
    """
    TODO: figure out why all records are being shown
    Retrive data from the database
    """
    data = (isbn,)
    sql_statement = """
    SELECT * FROM books WHERE (isbn == ?)
    """
    object = cur.execute(sql_statement, data)
    book = object.fetchone()
    con.commit()
    con.close()
    return book

def read_all_books():
    """
    Read all the books in the database
    """
    sql_statement = """
    SELECT * FROM books
    """
    object = cur.execute(sql_statement)
    data = object.fetchall()
    return data 

def update_book(pid:int, title:str=None, isbn:str=None, author_id:int=None, read_book:bool=None, comment:str=None):
    """
    Update fields in a book record
    """
    # this will be used to dynamically update data inside the database
    updates = []
    values = []

    if title is not None:
        updates.append("title = ?")
        values.append(title)

    if isbn is not None:
        updates.append("isbn = ?")
        values.append(isbn)
    if author_id is not None:
        updates.append("author_id = ?")
        values.append(author_id)

    if read_book is not None:
        updates.append("read_book = ?")
        values.append(read_book)

    if comment is not None:
        updates.append("comment = ?")
        values.append(comment)

    values.append(pid)

    sql_statement = """
    TODO
    """

def delete_book(isbn:str):
    """
    This function will delete a book based off of the ISBN
    """
    data = (isbn,)
    sql_statement = """
    DELETE FROM books WHERE isbn = ?
    """
    cur.execute(sql_statement, data) # excecutes SQL statement 
    con.commit() # commit data to database
    con.close() # close our connection
    return f"Data with ISBN: {isbn} deleted"

# Export all books in the database to CSV

def export_report(filename:str):
    """
    This function will output database to a CSV file
    """
    # pull all data from database
    # output of data to CSV
    # return a file to user 
    rows = read_all_books() # read all books in database
    column_names = ["id", "title", "author_id", "read_book", "comments", "isbn"] # set column names for csv file 

    # write CSV file
    with open(f"{filename}.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile) # use writer to create csv file
        csv_writer.writerow(column_names) # write the column names on the first row
        csv_writer.writerows(rows)
    print(f'Report named: {filename}.csv was generated')

    

if __name__ == "__main__":
 # create_book(title='A great book', isbn="0123456", author_id=1, comment='best book i have ever read!!')
 # create_book(title='Book 2', isbn="123456", author_id=1, comment='another book we read')
 # create_author(first_name='Aleyha', last_name='A.')
  # print(read_all_books())
  #print(delete_book(isbn="123456"))
  #print(read_book_record(isbn = "5655"))
 # export_report(filename='test')
 export_report(filename='report 1')