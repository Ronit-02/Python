# Classes and Instances
# 1. Each variable of a specific class is an instance or object.
# 2. Objects can have attributes, which store information about the object.
# 3. self -> current instance (class variable not local variable)

# Note: Always always initialize mutable attributes in the constructor 


class Apple:
    color = ""
    flavor = ""

golden = Apple()
golden.color = "red"
golden.flavor = "sweet"



# Instances

print()
class Clock:
    hours = 24
    def convert(self):
        print("{} hours = {} minutes".format(self.hours, self.hours*60))

clock1 = Clock()
clock1.hours = 4
clock1.convert()



# Constructors and Special Methods 

print()
class Person:
    def __init__(self, name, age):   # constructor
        """This is a piece of docstring"""
        self.name = name
        self.age = age
    def compare_age(self, other):   # Comparing object
        if self.age == other.age:
            print("They are equal")
    def __str__(self):               # for print statement
        return "This is {} who is {} years old.".format(self.name, self.age)
        
p1 = Person("Ronit", 20)
p2 = Person("Yash", 20)
p1.compare_age(p2)
print(p1)
# help(Person)



# Classes Example

print()
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.current #should output 1



# Inheritance

print()
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Grape(Fruit):
    pass

class Orange(Fruit):
    pass


print()
class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
          self.packages[package.name] = package
    def total_size(self):  
        result = 0
        for package in self.packages.values():
            result += package.size
        return result