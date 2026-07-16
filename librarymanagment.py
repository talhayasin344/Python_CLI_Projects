from datetime import datetime
import random

def printMenu():
    print("1. Add Book ")
    print("2. View Book ")
    print("3. Search Book ")
    print("4. Borrow Book ")
    print("5. Return Book ")
    print("6. Delete Book ")
    print("7. Exit ")

def generateISBN():
    characters="1234567890"
    store_isbn=""
    for i in range(13):
        gen_isbn=random.choice(characters)
        store_isbn += gen_isbn
    return store_isbn

def confirmAgain():
    confirm=input("Do you want to continue? yes/no? ")
    if confirm == "yes" or confirm == "Yes":
        return True
    elif confirm == "no" or confirm == "No":
        return False

books=[]
status="Available"
found=False

while True:
    printMenu()

    getinput=int(input("Select an option from above. "))
    if getinput == 1:
        getTitle=input("Enter the title of the book. ").title().strip()
        getDisc=input("Enter the description of the book. ").capitalize().strip()
        getAuthor=input("Who is the author of the book? ").capitalize().strip()
        current_year=datetime.now().year
        isbn=generateISBN()
        getGenre=input("What is the genre of this book? ").capitalize().strip()

        books.append({
            "title": getTitle,
            "disc": getDisc,
            "author": getAuthor,
            "currentyear": current_year,
            "isbn": int(isbn),
            "genre": getGenre,
            "status": status
        })
        print("Your book has been added successfully. ")
        if not confirmAgain():
            break
    elif getinput == 2:
        print("---------------- Book List ----------------")
        for i in range(len(books)):
            print(f"------------------------------------------------------------ ")
            print(f"{i}. The title of the book is {books[i]["title"]}")
            print(f"{i}. The description of the book is {books[i]["disc"]}")
            print(f"{i}. The author of the book is {books[i]["author"]}")
            print(f"{i}. The current year of the book is {books[i]["currentyear"]}")
            print(f"{i}. The isbn of the book is {books[i]["isbn"]}")
            print(f"{i}. The genre of the book is {books[i]["genre"]}")
            print(f"{i}. {books[i]["status"]}")
            print(f"------------------------------------------------------------ ")
        if len(books) == 0:
            print("No book found. ")
        if not confirmAgain():
            break
    elif getinput == 3:
        getSearch=input("Search the book you want. Either by name ").lower()
        for i in range(len(books)):
            if getSearch == books[i]["title"].lower():
                print(f"------------------------------------------------------------ ")
                print(f"The book name is {books[i]["title"]}")
                print(f"The book description is {books[i]["disc"]}")
                print(f"The book author is {books[i]["author"]}")
                print(f"The book current year is {books[i]["currentyear"]}")
                print(f"The book isbn is {books[i]["isbn"]}")
                print(f"The book genre is {books[i]["genre"]}")
                print(f"The book status is {books[i]["status"]}")
                print(f"------------------------------------------------------------ ")
                found=True
        if not found:
            print("Book not found. ")
        if not confirmAgain():
            break
    elif getinput == 4:
        get_isbn=int(input("Enter the ISBN number of the book you want to borrow. "))
        for book in range(len(books)):
            if get_isbn == books[book]["isbn"]:
                books[book]["status"]="Borrowed"
                print("Book is borrowed successfully. ")
        if not confirmAgain():
            break
    elif getinput == 5:
        getTheBookBack=int(input("Enter the ISBN number of the book to get it back. "))
        for book in range(len(books)):
            if getTheBookBack == books[book]["isbn"]:
                books[book]["status"]="Available"
                print("Book is Return successfully. ")
        if not confirmAgain():
            break
    elif getinput == 6:
        getdel_order=int(input("Enter the ISBN number to delete the book. "))
        for i in range(len(books)):
            if getdel_order == books[i]["isbn"]:
                books.pop(i)
        if not confirmAgain():
            break
    elif getinput == 7:
        break