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