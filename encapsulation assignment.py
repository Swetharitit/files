class Person:
    def __init__(self, name):
        self._name = name

    def display_name(self):
        print(f"Name: {self._name}")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
        
person = Person("John")
person.display_name()  
print(person.get_name())  
person.set_name("Jane")
person.display_name()

















class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_account_number(self, new_account_number):
        self._account_number = new_account_number

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            raise ValueError("Balance cannot be negative")
account = BankAccount("1234567890", 1000)
print(account.get_account_number())  
print(account.get_balance())  
account.set_balance(500)
print(account.get_balance())  
try:
    account.set_balance(-200)
except ValueError as e:
    print(e)
















class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def area(self):
        return self._width * self._height
rectangle = Rectangle(4, 5)
print(rectangle.width)  
print(rectangle.height) 
print(rectangle.area)  
rectangle.width = 3
print(rectangle.area)








class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 0 <= new_age <= 120:
            self._age = new_age
        else:
            raise ValueError("Age must be between 0 and 120")
student = Student("John", 20)
print(student.name)  
print(student.age)  
student.age = 25
print(student.age)  
try:
    student.age = -1
except ValueError as e:
    print(e)












class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
book = Book("To Kill a Mockingbird", "Harper Lee")
book.display()
book.title = "1984"
book.author = "George Orwell"
book.display()









class Employee:
    def __init__(self, name, position, salary=50000):
        self._name = name
        self._position = position
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


employee1 = Employee("John Doe", "Software Engineer")
print(employee1.name)  
print(employee1.position)  
print(employee1.salary)  

employee2 = Employee("Jane Smith", "Data Scientist", 60000)
print(employee2.name)  
print(employee2.position)
print(employee2.salary)














import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

# Example usage:
circle = Circle(5)
print(circle.radius)  
print(circle.circumference)  
circle.radius = 3
print(circle.circumference)












class Library:
    def __init__(self):
        self._books = []

    @property
    def books(self):
        return self._books.copy()

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only Book instances can be added")

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)
        else:
            raise ValueError("Book not found in library")

library = Library()
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
library.add_book(book1)
library.add_book(book2)
print(library.books)  
library.remove_book(book1)
print(library.books)  




        





    

