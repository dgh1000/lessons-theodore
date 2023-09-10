# character has a position and a name. It has 
# an inventory of items. Guns, etc. 

# Here's an example of a class that represents a person
# with a name and age.  The class has a method that returns
# the person's name and age as a string.
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name_and_age(self):
        return f"{self.name} is {self.age} years old."

# # Create a Person object and print the result of calling
# # its get_name_and_age method.
# name = "Joe"
# age = 34
person = Person("Joe", 34)
print(person.get_name_and_age())
#

# my_var1 = 10
# my_var2 = "a"
# my_var3 = 3.14
# print(f"age: {my_var1} name: {my_var2} pi: {my_var3}")
# print(my_var2)

# 1. Write a class called "Car" that has the following properties:
#    - a "color" property that is set in the constructor
#    - a "speed" property that is set in the constructor
#    - a "description" method that returns "{color} car going {speed} mph"
#    - a "accelerate" method that increases the speed by 1
#    - a "brake" method that decreases the speed by 1
#    - a "stop" method that sets the speed to 0


class Car:
    def __init__(self, color, speed,):
        self.color = color
        self.speed = speed

    def description(self):
        return f"a {self.color} car is going {self.speed} mph"

    def accelerate(self):
        self.speed = self.speed + 1

    def brake(self):
        self.speed = self.speed - 1

    
# Here's an example of using the class Car:
car = Car("red",     50)
print(car.description())
car.accelerate()
print(car.description())
car.brake()
print(car.description())

# car.brake()
# print(car.description())
# car.stop()
# print(car.description())

# 2. Write a class called "Rectangle" that has the following properties:
#    - a "width" property that is set in the constructor
#    - a "height" property that is set in the constructor
#    - a "area" method that returns the area of the rectangle
#    - a "perimeter" method that returns the perimeter of the rectangle
class Rectangle:
    def __init__(self, width, height,):
        self.width = width
        self.height = height

    def area(self):
        return f"the area of the rectangle is {self.width(self.height)}"
    
rectangle = Rectangle(5,5)
print(rectangle.area())
# Here's an example of using the class Rectangle:
# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# print(rectangle.perimeter())


