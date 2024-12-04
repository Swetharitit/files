class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


vehicle = Vehicle("Toyota", "Camry", 2020)
vehicle.display_info()










class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


car = Car("Honda", "Civic", 2018, 4)
car.display_info()

















class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year
    def display_info(self):
        print(f"Make: {self.__make}")
        print(f"Model: {self.__model}")
        print(f"Year: {self.__year}")


vehicle = Vehicle("Toyota", "Camry", 2020)
print(vehicle.get_make())  
vehicle.set_make("Honda")
print(vehicle.get_make())
vehicle.display_info()




















class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.__engine_size = engine_size

    
    def get_engine_size(self):
        return self.__engine_size

    
    def set_engine_size(self, engine_size):
        self.__engine_size = engine_size

    
    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.__engine_size}cc")

motorcycle = Motorcycle("Harley-Davidson", "Electra Glide", 2022, 1745)
motorcycle.display_info()













class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.__num_doors = num_doors

    

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.__num_doors}")
        print("Vehicle Type: Car")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.__engine_size = engine_size

    

    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.__engine_size}cc")
        print("Vehicle Type: Motorcycle")

car = Car("Honda", "Civic", 2018, 4)
car.display_info()

motorcycle = Motorcycle("Harley-Davidson", "Electra Glide", 2022, 1745)
motorcycle.display_info()        
