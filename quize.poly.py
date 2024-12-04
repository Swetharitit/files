class A:
    def show(self):
        print("A show")

class B(A):
    def shows(self):
        print("B show")

obj=B()
obj.show()







class Dog:
    def sound(self):
        return "Bark"
    
class Cat:
    def sound(self):
        return"Meow"
def make_sound(animal):
    print(animal.sound())

d=Dog()
c=Cat()
make_sound(d)
make_sound(c)













def check_number(num):
    if num > 0:
        return
    elif num < 0:
        return
    else:
        return
number=float(input("enter a number: "))
result=check_number(number)
print(result)









def even_numbers(start, end):
    if start > end:
        return []
    
    evens = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)

    return evens

print(even_numbers(2, 10))
print(even_numbers(10, 2))
print(even_numbers(3, 7))






















import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    area = math.pi * radius ** 2
    return area


radius = float(input("Enter the radius of the circle: "))


area = calculate_circle_area(radius)


print(f"The area of the circle with radius {radius} is {area:.2f}")
    


