from utils import database

USER_CHOICE = """
Your Choices are the following :
- "a" to add a new book
- "l" to list all books
- "r" to mark a book as read
- "d" to delete the book
- "q" to exit

Enter Your Choice:"""

#Defining Function for providing options to theuser
def menu():
    database.create_books_table()
    user_input = input(USER_CHOICE).strip()
    while user_input != "q":
        if user_input == "a":
            add_book()
        elif user_input == "l":
            books_list()
        elif user_input == "r":
            read_book()
        elif user_input == "d":
            delete_book()
        else:
            print("Wrong Input , please try again!!!")
        user_input = input(USER_CHOICE)


# Adds the book you entered in the Database
def add_book():
    book_name = input("Enter the name of the book: ").strip()
    author_name = input("Enter the name of the Author: ").strip()

    database.add_books(book_name, author_name)

#Print the list of books present in the database
def books_list():
    books = database.get_all_books()
    for book in books:
        read = "YES" if book["read"] == 1 else "NO"
        print(f"{book['book_name']} is written by {book['author_name']}, read: {read}")

#If the the has been read already then it will be marked as read
def read_book():
    book_name = input("Enter the name of the book you have read already: ").strip()

    database.mark_as_read(book_name)

#Delete the book you want to delete from the database
def delete_book():
    book_name = input("Enter the name of the book you want to delete: ").strip()
    books = database.get_all_books()
    for book in books:
        database.delete_the_book(book_name)

#Driver Function
if __name__ == "__main__":
    menu()

