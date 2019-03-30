class my_class:
    x = 5
    y = 10


p1 = my_class()
print(my_class.y)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Richie", 29)

print(p1.name)
print(p1.age)


class Car:
    def __init__(self, make, age):
        self.make = make
        self.age = age

    def myfunc(self):
        print("We own a " + self.make)

toyota = Car("Toyota", "new")
print(toyota.age)
pontiac = Car("Pontiac", "older")
print(pontiac.make)



pontiac.make

my_name = "My name {} {}"
print(my_name.format("Richie", "Young"))