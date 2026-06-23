# function => the block of code that executes whenever we call it
# DRY => Don't repeat yourself

# rule for defining function
# function defination or declaration
# function call

# syntax:
# def function_name(parameter1, parameter2, ... , parameterN):
#     block of code to execute

# function_name(arg1,arg2,..., argN)

# def add():
#     a = 10
#     b = 20
#     c = a + b
#     print(c)

# add()

# add()


# def greet(name):
#     print("Hello and namaste ", name)

# greet("Ares")
# greet("Simran")
# greet("Shyam")

# def login(username, password):
#     if username == "ares" and password == "ares@123":
#         print("Welcome back Ares")
#     else:
#         print("Hello other users")


# username = input("Enter your username: ")
# password = input("Enter your password: ")
# login(username,password)


# write a program to make simple calculator using function
# write a program to find positive, negative or zero using function and return the value

# return

# def add(first_number, second_number):
#     return first_number + second_number

# a = add(10,20)

# if a > 10:
#     print("The sum is greater than 10")

# def greatest_number(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# result = greatest_number(10,20,30)
# print("The greatest number is ", result)

# positional argument => argument that comes in position

# keyword/named argument => argument that comes with name of parameter

# def student_information(name, college, course):
#     print(name, college, course)

# # student_information("Ares","ISMT","Full stack")

# student_information(college="ISMT",name="Ares", course="full stack")


# *args and **kwargs

# def add(a,b,*args):
#     print(a)
#     print(b)
#     print(args)


# add(1,2,3,4,5,6,7,8,9,10)
# def student_info(a,b, *args, name, age,**kwargs):
#     print(args)
#     print(kwargs)

# student_info(1,2,3,4,5,name="Ares", age=12, course="python",fee="25000",college="ISMT",company="Devsign")



# *args and **kwargs
# def add(a,b,*args):
#     print(args)

# add(1,2,3,4,5,6,7,8,9,10)

# named argument **kwargs

# def student_info(a,b,*args,name, age,**kwargs):
#     print(kwargs)
#     print(args)

# student_info(1,2,3,4,5,6,7,name="Ares", age=12, course="python",fee="25000",college="ISMT",company="Devsign")