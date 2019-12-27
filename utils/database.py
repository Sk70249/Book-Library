from utils.database_connection import DatabaseConnection
''''
    Connecting and retrieving books for Database
'''
#books_file = "books.txt"

def create_books_table():
    with DatabaseConnection("data.db") as connection: #This is an "CONTEXT MANAGER" for opening and closing connection.
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(book_name text primary key, author_name text, read integer)")



def add_books(book_name, author_name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (book_name, author_name))



def get_all_books():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")

        books = [{"book_name":row[0], "author_name":row[1], "read":row[2]} for row in cursor.fetchall()]

    return books


def mark_as_read(book_name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE book_name=?", (book_name,))



def delete_the_book(book_name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE book_name=?",(book_name,))

