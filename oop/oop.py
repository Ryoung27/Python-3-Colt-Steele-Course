class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound("MEOW")
print(blue.cool)

print(isinstance(blue, Animal))
print(isinstance(blue, object))

#Properties

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         if age >= 0:
#             self._age = age
#         else:
#             self._age = 0

#     def get_age(self):
#         return self._age

#     def set_age(self, new_age):
#         if new_age >= 0:
#             self._age = new_age
#         else:
#             self._age = 0

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self._age = value
#         else:
#             raise ValueError("age can't be negative")

# jane = Human("Jane", "Goodall", 50)
# print(jane.age)