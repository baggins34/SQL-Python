"""
İbrahim Halil Bayat, PhD
İstanbul Technical University
İstanbul, Turkey

"""
import sqlite3
import time

class class_book():
    def __init__(self, name, writer, publisher, genre, press):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.genre = genre
        self.press = press
    def __str__(self):
        return "Name of the Book: {}\nWriter of the Book: {}\nPublisher of the Book: {}\nGenre of the Book: {}\nNumber of the Press: {}\n".format(self.name, self.writer, self.publisher, self.genre, self.press)

class class_library():
    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()
        check = "Create Table If not exists table_books (name TEXT,writer TEXT,publisher TEXT,genre TEXT,press INT)"
        self.cursor.execute(check)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def show_books(self):
        check = "select * from table_books"
        self.cursor.execute(check)
        list_books = self.cursor.fetchall()
        if len(list_books) == 0:
            print("No Books")
        else:
            for i in list_books:
                i_book = class_book(i[0], i[1], i[2], i[3], i[4])
                print(i_book)
                print("-----------------------------------------------------------")

    def check_book(self, name):
        check = "select * from table_books where name = ?"
        self.cursor.execute(check,(name,))
        list_books = self.cursor.fetchall()
        if len(list_books) == 0:
            print("There is no such book.")
        else:
            book = class_book(list_books[0][0], list_books[0][1], list_books[0][2], list_books[0][3], list_books[0][4])
            print(book)

    def add_book(self, book):
        check = "insert into table_books Values(?,?,?,?,?)"
        self.cursor.execute(check, (book.name, book.writer, book.publisher, book.genre, book.press))
        self.connection.commit()

    def delete_book(self, d_name ):
        check = "delete from table_books where name= ?"
        self.cursor.execute(check, (d_name,))
        self.connection.commit()

    def press_up(self, p_name):
        check = "select * from table_books where name = ?"
        self.cursor.execute(check, (p_name, ))
        list_books = self.cursor.fetchall()
        if len(list_books) == 0:
            print("There is no such book")
        else:
            press = list_books[0][4]
            press += 1

            check2 = "update table_books set press = ? where name = ?"
            self.cursor.execute(check2, (press, p_name ))
            self.connection.commit()