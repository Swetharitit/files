import math

class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.__radius


circle = Circle(5)
print("Radius:", circle._Circle__radius)
print("Area:", circle.calculate_area())
print("Circumference:", circle.calculate_circumference())

circle.set_radius(10)
print("New Radius:", circle._Circle__radius)
print("New Area:", circle.calculate_area())
print("New Circumference:", circle.calculate_circumference())

















class Employee:
    def __init__(self, name="", salary=0):
        self.__name = name
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def calculate_yearly_salary(self):
        return self.__salary * 12

employee = Employee("John Doe", 5000)
print("Name:", employee.get_name())
print("Monthly Salary:", employee.get_salary())
print("Yearly Salary:", employee.calculate_yearly_salary())

employee.set_name("Jane Doe")
employee.set_salary(6000)
print("New Name:", employee.get_name())
print("New Monthly Salary:", employee.get_salary())
print("New Yearly Salary:", employee.calculate_yearly_salary())
















class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} removed from library.")
                return
        print(f"{title} not found in library.")
    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")


library = Library()
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.display_books()
library.remove_book("1984")
library.display_books()
















class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero!")


calculator = Calculator()
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
print("Division:", calculator.divide(6, 3))

try:
    print("Division by zero:", calculator.divide(6, 0))
except ValueError as e:
    print(e)
























class Movie:
    def __init__(self, title="", rating=""):
        self.__title = title
        self.__rating = rating

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_rating(self, rating):
        self.__rating = rating

    def get_rating(self):
        return self.__rating

    def display_details(self):
        print(f"Title: {self.__title}")
        print(f"Rating: {self.__rating}")
        
movie = Movie("The Shawshank Redemption", "PG")
print("Title:", movie.get_title())
print("Rating:", movie.get_rating())
movie.display_details()

movie.set_title("The Godfather")
movie.set_rating("R")
print("New Title:", movie.get_title())
print("New Rating:", movie.get_rating())
movie.display_details()






















import math

class Circle:
    def calculate_area(self, radius):
        
        area = math.pi * (radius ** 2)
        return area


circle = Circle()
radius = 5
print(f"Area of circle with radius {radius}: {circle.calculate_area(radius)}")



































class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        
        celsius = (fahrenheit - 32) * 5/9
        return celsius


temperature = Temperature()
celsius = 30
print(f"{celsius}°C is equal to {temperature.celsius_to_fahrenheit(celsius)}°F")

fahrenheit = 86
print(f"{fahrenheit}°F is equal to {temperature.fahrenheit_to_celsius(fahrenheit)}°C")

























class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if name in self.items:
            
            updated_quantity = self.items[name]['quantity'] + quantity
            self.items[name]['quantity'] = updated_quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name, quantity):
        if name in self.items:
    
            updated_quantity = self.items[name]['quantity'] - quantity
            if updated_quantity <= 0:
                del self.items[name]
            else:
                self.items[name]['quantity'] = updated_quantity
    def calculate_total(self):
        
        total_cost = 0
        for item in self.items.values():
            total_cost += item['price'] * item['quantity']
        return total_cost


cart = ShoppingCart()
cart.add_item('Apple', 1.00, 2)
cart.add_item('Banana', 0.50, 3)
print("Total:", cart.calculate_total())
cart.remove_item('Apple', 1)
print("Total:", cart.calculate_total())















class Number:
    def is_prime(self, num):
        
        is_prime = True
        if num < 2:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        return is_prime


number = Number()
print("Is 25 prime?", number.is_prime(25))
print("Is 23 prime?", number.is_prime(23))























class Password:
    def check_strength(self, password):
        
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special_char = False
        meets_length_req = False

    
        if len(password) >= 8:
            meets_length_req = True

        
        for char in password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special_char = True
 
        if (has_uppercase and has_lowercase and has_digit and has_special_char and meets_length_req):
            return "Strong"
        else:
            return "Weak"


password = Password()
print("Password 'P@ssw0rd' strength:", password.check_strength("P@ssw0rd"))
print("Password 'password' strength:", password.check_strength("password"))
                
        
