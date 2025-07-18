class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self): 
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):  
        return "Meow! Meow!"


animal = Animal()
dog = Dog()
cat = Cat()

print(f"Animal: {animal.make_sound()}")
print(f"Dog: {dog.make_sound()}")
print(f"Cat: {cat.make_sound()}")