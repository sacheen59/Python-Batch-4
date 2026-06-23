# oops => object oriented programming
# abstraction => hiding the internal details
# encapsulation => binding the data and its method inside a class
# inheritance => sharing the data between two or more classes
# polymerphism => having more than one form

# class => blueprint for the properties and methods
# object => instance of a class


# class Animal:

#     def display(self):
#         print("this is display")


# obj = Animal()
# obj.display()

# obj1 = Animal()
# obj1.display()


# # obj = Animal()
# # # obj1 = Animal()
# # # print(obj.name)
# # obj.display()
# # obj1.display()


# # class StudentInfo:

# #     def display_student_details(self,name,age,address):
# #         print(f"Name: {name}")
# #         print(f"Age: {age}")
# #         print(f"Address: {address}")


# # ares = StudentInfo()
# # ares.display_student_details("Ares",12,"Kaosati")
# # simran = StudentInfo()
# # simran.display_student_details("Simarn",10,"Beldiya")


# class Area:

#     PI = 3.14

#     def area_of_rectangle(self,length, breadth):
#         return length * breadth

#     def area_of_square(self,length):
#         return length ** 2

#     def area_of_circle(self, radius):
#         return Area.PI * (radius ** 2)


# circle = Area()
# area_of_circle = circle.area_of_circle(5)
# print(f"The area of circle: {area_of_circle}")

# rectangle = Area()
# area_of_rectangle = rectangle.area_of_rectangle(10,20)
# print(f"The area of rectangle: {area_of_rectangle}")

# square = Area()
# area_of_square = square.area_of_square(5)
# print(f"The area of square: {area_of_square}")


# initializer/constructor => it is the method of an class that is called whenever the object is made for the first time

# class StudentInfo:

#     def __init__(self,name):
#         self.name = name
#         print(self.name)

#     def example(self):
#         print("We need to call it manually")

#     def __str__(self):
#         return f"This is object of {self.name}"


# ares = StudentInfo("Ares")
# print(ares)

# simran= StudentInfo('simran')
# print(simran)
# simran = StudentInfo("simran")
