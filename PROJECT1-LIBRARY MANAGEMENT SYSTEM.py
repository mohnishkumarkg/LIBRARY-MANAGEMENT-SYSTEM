

# We will build:
# Phase 1 (Core System)
# Book class
# Library class
# Add book
# View books
# Issue book
# Return book
# Store data in file
# Prevent duplicate books
# Track issued status properly
# Book Class – Proper Design
# A Book should have:

# book_id        → unique number (very important)
# title          → name of book
# author         → writer
# is_issued      → True / False
# issued_to      → name of student (None if not issued)




#Book class with the above mentioned attributes and methods to display details, borrow and return book.




from  datetime import date,datetime,timedelta
from colorama import Fore,Style
import time
print(Fore.GREEN + "Welcome to the Library Management System!" + Style.BRIGHT)
print()
time.sleep(2)
#--------EXCEPTION CLASSES----------------
class BookNotFoundError(Exception):
    def __init__(self,book_id):
        self.book_id=book_id
    def __str__(self):
        return (Fore.RED + f"❌Book with ID {self.book_id} not found in the library." + Style.BRIGHT)
    
class BookAlreadyborrowed(Exception):
    def __init__(self,book_id,issued_to):
        self.book_id=book_id
        self.issued_to=issued_to
    def __str__(self):
        return (Fore.YELLOW + f"⚠ Book with ID {self.book_id} is already issued to {self.issued_to}." + Style.BRIGHT)
    
class BookAlreadyExists(Exception):
    def __init__(self,book_id):
        self.book_id=book_id
    def __str__(self):
        return (Fore.RED + f"⚠ Book with ID {self.book_id} already exists in the library." + Style.BRIGHT)
class BookNotBorrowed(Exception):
    def __init__(self,book_id):
        self.book_id=book_id
    def __str__(self):
        return (Fore.RED + f"❌Book with ID {self.book_id} was not borrowed, so it cannot be returned." + Style.BRIGHT)
    
class StudentNotRegisteredError(Exception):
    def __init__(self,student_name):
        self.student_name=student_name
    def __str__(self):
        return (Fore.RED + f"❌Student with name {self.student_name} is not registered in the library." + Style.BRIGHT)

#--------------------BOOK CLASS-----------------------
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_issued=False
        self.issued_to=None
        self.issuedate=None
        self.duedate=None
        self.borrowed_timing=None

    #test 
    def display_details(self):             #displaying the details of the book
        print(f"Book ID:{self.book_id}")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Available:{self.is_issued}")
    
    def get_details(self):                 #returning the details of the book in a tuple format 
        return ( f"BOOK ID :{self.book_id}",
                 f"TITLE:{self.title}",
                 f"AUTHOR:{self.author}",
                 f"AVAILABLE:{self.is_issued}"
        ) 
    
    def borrow_book(self,student_name):                 #Avaialbilty check of the book for borrowing

        if(self.is_issued==False):

            print("Book is available for borrowing.")
            self.is_issued=True
            self.issued_to=student_name

        else:
            print(Fore.RED + f"Book is currently not available for borrowing. issued to: {self.issued_to}" + Style.BRIGHT)
    
    def return_book(self):                #returning the book and making it available for borrowing again
        if(self.is_issued ==True):
            print(Fore.GREEN + f"✔ Book is being returned by {self.issued_to}." + Style.RESET_ALL)
            time.sleep(2)
            self.is_issued=False
            self.issued_to=None
        else:
            print(Fore.YELLOW + "⚠ Book was not borrowed." + Style.RESET_ALL)
            time.sleep(1)
#skeleton of Library class
# - Hold a collection of books.
# - Add new books.
# - Show all books.
# - Find a book by ID or title.
# - Borrow/return books through the library interface.
 
#------------STUDENT CLASS------------------------
class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.borrowed=[]

    def borrow_book(self,book):
        self.borrowed.append(book)

    def return_book(self,book):
        if book in self.borrowed:
            self.borrowed.remove(book)
    def display_borrowedbooks(self):
        if(self.borrowed):
            print(f"The books borrowed by {self.name} are:")
            for borrowed_book in self.borrowed:
                print(Fore.CYAN + f"Book ID:{borrowed_book.book_id}, Name of the Book:{borrowed_book.title},Author:{borrowed_book.author}" + Style.RESET_ALL)
                time.sleep(1)
        else:
            print(f"{self.name} has not borrowed any books.")
            time.sleep(1)
#-------LIBRARY CLASS----------------

class Library:
    def __init__(self):
        self.books=[]
        self.students=[]
    
    def add_student(self,student):
        self.students.append(student)

    def add_book(self,book):     
        for  existing_book in self.books:#checking for duplicates
            if(existing_book.book_id==book.book_id):
                raise BookAlreadyExists(book.book_id)
                           #adding book to library collection

        self.books.append(book)

        print(f"Book named '{book.title}' added to the library.")
        print()
        time.sleep(1)
    def Display_books(self):                 #displaying the entire book collection of library

        print(Fore.CYAN + "📚Available Books in the Library:" + Style.RESET_ALL)
        for book in self.books:
            print(f"Book ID:{book.book_id}, Title:{book.title}, Author:{book.author}, Available:{book.is_issued}")
            print()
        time.sleep(1)

        
    def search_book(self,book_id):
        found=False
        for existingbook in self.books:
                if(existingbook.book_id==book_id):
                        return existingbook
        raise BookNotFoundError(book_id)
    
    def find_student(self,student_name):
        for student in self.students:
            if(student.name==student_name):
                return student
        raise StudentNotRegisteredError(student_name)
    
    def borrow_book(self, book_id, student_name):
        book = self.search_book(book_id)
        if book.is_issued:
            raise BookAlreadyborrowed(book_id, book.issued_to)

        student = self.find_student(student_name)

        book.is_issued = True
        book.issued_to = student.name
        book.issuedate = date.today()
        book.duedate = book.issuedate + timedelta(days=14)
        book.borrowed_timing = datetime.now()
        student.borrow_book(book)

        print(f"{Fore.GREEN}✔ Book Info:({book.title}, {book.author}, {book.book_id}) borrowed successfully by {student.name}.{Style.RESET_ALL}")
        print()
        time.sleep(2)

    def return_book(self,book_id):
        book = self.search_book(book_id)
        if not book.is_issued:
            raise BookNotBorrowed(book_id)
        if book.issued_to is None:
            raise StudentNotRegisteredError("No student")  # or handle gracefully
        student = self.find_student(book.issued_to)
       
                                  
        print(f"{Fore.GREEN}✔ Book is being returned by {book.issued_to}.{Style.RESET_ALL}")
        print()
        time.sleep(2)
        student.return_book(book)
        book.borrowed_timing=None
        book.issuedate=None
        book.is_issued=False
        book.duedate=None
        book.issued_to=None
       
    
    def total_books(self):
        return len(self.books)
    
    
    def issued_books(self):
        issued_books=[ book for book in self.books if book.is_issued]
        count_of_issued_books=len(issued_books)
        available_books=len(self.books)-count_of_issued_books

        return issued_books,count_of_issued_books,available_books
    
    def borrowing_history(self):
        history=[]
        for book in self.books:
            if book.is_issued:
                history.append((book.book_id,book.title,book.issued_to))
        if(history):
        
            return history
        return "No borrowing history available."
    
    def overdue_books(self):
        today=date.today()
        overdue_books=[(book,f"borrowed by {book.issued_to}") for book in self.books if book.is_issued and book.duedate<today]
        if len(overdue_books)>0:
            return overdue_books
        return "No overdue books at the moment."
    
    def report_issued_books(self):
        L=[(book.book_id, book.title, book.issued_to, book.duedate) for book in self.books if book.is_issued]
        if(L):
            return [(book.book_id, book.title, book.issued_to, book.duedate) for book in self.books if book.is_issued]
        return "No books are currently issued."
    


Library_storage=Library()

book1=Book(1,"The Great Gatsby","F. Scott Fitzgerald")

Library_storage.add_book(book1)
book2=Book(2,"To Kill a Mockingbird","Harper Lee")

book3=Book(3,"Around the world in 80 days"," Jules Verne")

Library_storage.add_book(book2)
Library_storage.add_book(book3)



s1=Student(101,"Mohnish")

s2=Student(102,"Ajay")

s3=Student(103,"Rohit")
s4=Student(104,"Sonia")
s5=Student(105,"Priya")
Library_storage.add_student(s1)

Library_storage.add_student(s2)

Library_storage.add_student(s3)
Library_storage.add_student(s4)
Library_storage.add_student(s5)


try:
    Student=Library_storage.find_student("Mohnish")
    print(f"{Fore.GREEN}✔ Student found: {Student.name}{Style.RESET_ALL}")
    print()
    time.sleep(2)
except StudentNotRegisteredError as e:
    print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
    print()
    time.sleep(2)
try:
    Library_storage.borrow_book(1,"Mohnish")
    Library_storage.borrow_book(2,"Ajay")
  # Attempting to borrow an already issued book

    
except BookAlreadyborrowed as e:
    print(f"{Fore.YELLOW}⚠ Warning: {e}{Style.RESET_ALL}")
    print()
    time.sleep(2)

try:
    Library_storage.add_book(Book(1,"The Great Gatsby","F. Scott Fitzgerald"))
    
except BookAlreadyExists as e:
    print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
    print()
    time.sleep(2)

try:
    Library_storage.return_book(2)  # Attempting to return a book that was not borrowed
    Library_storage.return_book(1)

except BookNotBorrowed as e:
    print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
    print()


Library_storage.Display_books()

print(f"{Fore.BLUE}📖 Borrowing History:{Style.RESET_ALL}")
print(Library_storage.borrowing_history())
print()
time.sleep(2)
print(f"{Fore.BLUE}📅 Overdue Books:{Style.RESET_ALL}")
print(Library_storage.overdue_books())
print()
time.sleep(2)
print(f"{Fore.BLUE}📋 Issued Books Report:{Style.RESET_ALL}")
print(Library_storage.report_issued_books())
print()
time.sleep(2)


s1.display_borrowedbooks()
s2.display_borrowedbooks()
# Phase 2 is all about User Management—this is where your library system grows beyond just books and starts handling the people who interact with it.

# 🎯 Goals of Phase 2
# - Introduce a User (or Student) class.
# - Track which users are registered in the library.
# - Connect users to the books they borrow.
# - Enforce rules with new exceptions (like UserNotRegisteredError)
