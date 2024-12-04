class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 30)

print(person.name)  
print(person.age)



















a = [1, 2, 3]
b = a
b.append(4)
print(a)







def append_element(lst):
    lst.append(4)

a = [1, 2, 3]
append_element(a)
print(a)







def increment(n):
    n += 1

a = 5
increment(a)
print(a)













class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

person = Person("John")
person.greet()
class Person:
    def __init__(person_ref, name):
        person_ref.name = name

    def greet(person_ref):
        print(f"Hello, my name is {person_ref.name}")

person = Person("John")
person.greet()













class Person:
    def __init__(self, name="John Doe", age=30):
        self.name = name
        self.age = age


person1 = Person()
print(person1.name)  
print(person1.age)


person2 = Person("Jane Doe", 25)
print(person2.name)  
print(person2.age)











class Person:
    def __init__(self, name=None):
        if name is None:
            self.name = "John Doe"
        else:
            self.name = name
















a = [1, 2, 3]
b = a
a.append(4)
print(b)


a = "hello"
b = a
a += " world"
print(b)













class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

a = Singleton()
b = Singleton()
print(a is b)















def modify_list(lst):
    lst.append(4)

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)

















class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.profile_data = self._load_profile_data()  

    def _load_profile_data(self):
        
        return {'key1': 'value1', 'key2': 'value2', ...':'}




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._profile_data = None  

    @property
    def profile_data(self):
        if self._profile_data is None:
            self._profile_data = self._load_profile_data()
        return self._profile_data

    def _load_profile_data(self):
        
        return {'key1': 'value1', 'key2': 'value2', ...}    

