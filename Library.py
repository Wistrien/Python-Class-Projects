# INFO-1298 Python
# Project 1
# Author: Charles Millar
# This program is for the management of a personal book library system.

from os import system, name
from time import sleep
from datetime import date

# Library dictionary
library = {}
# current year
current_year = date.today().year


# While loop for the main menu from https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
def main_menu():
    while True:
        menu()


# Screen clear function from https://www.geeksforgeeks.org/python/clear-screen-python/
def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# Return to main menu function
def return_menu():
    print()
    input("ENTER to return to the main menu")


# Book add fail function
def book_addf():
    print("Book addition Failed")
    input("Press ENTER to return to the main menu")


# Menu Options Logic
# BC = Before Check
# Function to add a book to the library
def add_book():
    clear_screen()
    # Title Check
    title = input("Enter book title: ").strip().title()
    if title == "":
        print("title can't be blank")
        book_addf()
        return
    if title in library:
        print(title, "is already in the library.")
        input("Press ENTER to return to the main menu")
        return
    # Author Check
    author_BC = input("Enter the author's name: ").strip()
    if author_BC != "":
        author = author_BC.title()
    else:
        print("Author must not be  blank")
        book_addf()
        return
    # Year Check
    year_BC = input("Enter release year: ").strip()
    if year_BC.isdigit() != True:
        print("Year must be a number")
        book_addf()
        return
    elif int(year_BC) < 1000 or int(year_BC) > current_year + 1:
        print("Invalid year")
        book_addf()
        return
    else:
        year = int(year_BC)
    # ISBN Check
    isbn_BC = input("Enter ISBN: ").strip()
    if isbn_BC.isdigit() != True:
        print("ISBN must be a number")
        book_addf()
        return
    elif len(isbn_BC) < 10:
        print("ISBN must be at least 10 characters long")
        book_addf()
        return
    else:
        isbn = isbn_BC
    library[title] = {
        "author": author,
        "year": year,
        "isbn": isbn,
    }
    print(title, "has been added to the library.")
    return_menu()


# Function to update the author of a given book
def update_author():
    clear_screen()
    title = input("Enter book title: ")
    if title in library:
        author_check = input("Enter the new author's name: ").strip()
        if author_check != "":
            library[title]["author"] = author_check.title()
            print("author has been updated")
        else:
            print("Author can't be blank")
            return_menu()
            return
    else:
        print(title, "is not in the library.")
    return_menu()


# Function to update the release year of a given book
def update_year():
    clear_screen()
    title = input("Enter book title: ")
    if title in library:
        year_check = input("Enter the new release year: ")
        if year_check.isdigit() != True:
            print("Year must be a number")
            return
        elif int(year_check) < 1000 or int(year_check) > current_year + 1:
            print("Invaild year")
            return
        else:
            library[title]["year"] = int(year_check)
            print("release year has been updated")
    else:
        print(title, "is not in the library.")
    return_menu()


# Function to search the library for a given book
def search_title():
    clear_screen()
    title = input("Enter Book Title: ").strip().title()
    if title in library:
        book = library[title]
        print("Title:", title, sep="\n")
        print("Author:", book["author"], sep="\n")
        print("Release Year:", book["year"], sep="\n")
        print("ISBN:", book["isbn"], sep="\n")
    else:
        print("Book not in library")
    return_menu()


# Function to remove a book from the library
def delete_book():
    clear_screen()
    title = input("Type the book you want to delete: ").strip().title()
    if title in library:
        confirmation = input("Are you sure you want to delete this book (Y/N): ").strip().lower()
        if confirmation == "y":
            del library[title]
            print(title, "has been removed")
            return_menu()
        elif confirmation == "n":
            print("Canceling")
            sleep(1)
    else:
        print("Book name invaild")
        return_menu()


# Function to display all of the books in the library
def display_books():
    clear_screen()
    if len(library) == 0:
        print("The library is empty")
    else:
        print("Books in the library:", "", sep="\n")
        for title in sorted(library.keys()):
            book = library[title]
            print("  Title:", title)
            print("    Author:", book["author"])
            print("    Release Year:", (book["year"]))
            print("    ISBN:", book["isbn"])
            print()
    return_menu()


# Function to exit the program
def exit_program():
    confirmation = input("Are you sure you want to exit? (Y/N): ").strip().lower()
    if confirmation == "y":
        exit()
    elif confirmation == "n":
        print("Canceling")
        sleep(1)
    else:
        print("Invalid Selection Canceling")
        sleep(1)


# Dictionary for menu options
menu_options = {
    1: add_book,
    2: update_author,
    3: update_year,
    4: search_title,
    5: delete_book,
    6: display_books,
    7: exit_program,
}


# Selection Logic
def menu_select():
    menu_selection = input("Input your selection: ")
    if menu_selection.isdigit() == False:
        print("Please enter a number")
        sleep(1)
    elif int(menu_selection) in menu_options:
        menu_options[int(menu_selection)]()
    else:
        print("Please make a valid selection")
        sleep(1)


# Menu
def menu():
    clear_screen()
    print(r"""
      _.--._  _.--._
,-=.-':;:;:;\':;:;:;'-._
\\\:;:;:;:;:;\:;:;:;:;:;\
 \\\:;:;:;:;:;\:;:;:;:;:;\
  \\\:;:;:;:;:;\:;:;:;:;:;\
   \\\:;:;:;:;:;\:;::;:;:;:\
    \\\;:;::;:;:;\:;:;:;::;:\
     \\\;;:;:_:--:\:_:--:_;:;\
      \\\_.-'      :      '-._\
       \`_..--''--.;.--''--.._=>
    """)
    print("Welcome to the library!", "Options", sep="\n\n")
    print(
        "1. Add a book",
        "2. Update a book's author",
        "3. Update a book's publication year",
        "4. Search for a book by title",
        "5. Delete a book",
        "6. Display all books (Sorted by title)",
        "7. Exit",
        sep="\n",
    )
    menu_select()


# Call menu
main_menu()
# https://www.geeksforgeeks.org/python/title-in-python/
# https://www.w3schools.com/python/ref_string_strip.asp
# https://www.w3schools.com/python/ref_string_isdigit.asp
