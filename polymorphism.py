

# class Animal:

#     def sound(self):
#         return "A generic sound"

# class Dog(Animal):

#     def sound(self):
#         print(super().sound())
#         return "Bark"

# obj = Dog()
# print(obj.sound())


# class Cat(Animal):

#     def sound(self):
#         return "Meow"

# animals = [Animal(), Dog(), Cat()]


# for animal in animals:
#     print(animal.sound())


class Practice:

    def __init__(self):
        self._age = 0

    def get_age(self):
        print("Getter method called")
        return self._age

    def set_age(self, x):
        print("setter method called")
        self._age = x

    age = property(get_age, set_age)


obj = Practice()
obj.age = 20
print(obj.age)
