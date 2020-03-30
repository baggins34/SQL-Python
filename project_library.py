from library import *
print("""
Welcome to the Library program.
A program to help you add, see, delete and update the books in the library of your SQL database 
by 
İbrahim Halil Bayat, PhD
İstanbul Technical University 
İstanbul, Turkey 
*********************************
Please enter the related number for your action

1. Show the books

2. Check a book 

3. Add a new book 

4. Delete a book from the library

5. Increase the number of a book's press

Please press 'q' to exit.

""")

obj_library = class_library()

while True:
    operation = input("The number of the action: ")
    if operation == "q":
        print("Th program ends.")
        time.sleep(2)
        print("The program is ended")
        print("Good Bye....")
        break

    elif operation == "1":
        print("1. Show the books")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        obj_library.show_books()

    elif operation == "2":
        print("2. Check a book")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        name = input("Please enter the name of the book you want to check: ")
        print("Name: ",name)
        time.sleep(2)
        obj_library.check_book(name)

    elif operation == "3":
        print("3. Add a new book")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        name = input("Name of the book: ")
        writer = input("Writer of the book: ")
        publisher = input("Publisher of the book: ")
        genre = input("Genre of the book: ")
        press = int(input("Press of the book: "))
        new_book = class_book(name, writer, publisher, genre, press)
        print("Adding the book...")
        time.sleep(2)
        obj_library.add_book(new_book)
        print("The book is added to the library.")

    elif operation == "4":
        print("4. Delete a book from the library")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        name = input("Name of the book you want to delete: ")
        check = input("Are you sure. Please enter 'yes' or 'no': ")
        if check ==  "yes":
            print("Deleting", name)
            time.sleep(2)
            obj_library.delete_book(name)
            print("The book is deleted")

    elif operation == "5":
        print("5. Increase the number of a book's press")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        name = input("Please enter the name of the book: ")
        print("Increasing the number of the press...")
        time.sleep(2)
        obj_library.press_up(name)
        print("The number of the book is increased.")
    else:
        print("Please enter a valid action number")