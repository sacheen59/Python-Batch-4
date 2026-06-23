# function => reusable block of code that is executed whenever it is called.
# function declaration and defination
# function call

# parameter => formal value that is used in function declaration/defination
# argument => actual value that is used in function call

# def function_name(para1, para2, ...., paraN):
    # block of code

# function_name(arg1, arg2,..., argN)

# def sum(a,b):
#     print(a + b)

# sum(10,20)

# return in python function

# def sum(a,b):
#     return a + b

# result = sum(10,20)
# print(result)

# function as a first class citizen
# 1. can be stored in variable
# 2. can be passed as argument
# 3. can return from another function

# def outer_function(func, num):
#     if num == 30:
#         return func

# # def greet():
# #     print("Hello and namaste")

# def add():
#     print(10 + 20)

# # result = outer_function(greet)
# # result()

# sum = outer_function(add, 30)
# sum()

# def login(func , username, password):
#     if username == "admin" and password == "admin@123":
#         return func


# def add_product():
#     print("Product added successfully")

# def remove_product():
#     print("Product deleted successfully")


# username = input("Enter your username: ")
# password = input("Enter your password: ")

# output = login(add_product, username, password)



# decorator => it is a higher order function that is use to extend or modify the behaviour of existing function
# 1. Normal decorator

# def my_decorator(func):
#     def wrapper(name):
#         if name == "Ares":
#             func(name)
#         else:
#             print("You are not a ares")

#     return wrapper


# @my_decorator
# def greet(name):
#     print("Hello",name)

# @my_decorator
# def nepali_greet():
#     print("Dhog garey")


# greet("Ares")

# nepali_greet()

def admin_only(username,password):
    def outer_function(func):
        def wrapper(product_name):
            if username == "admin" and password == "admin@123":
                func(product_name)
            else:
                print("you are not authorized to do this action")
        return wrapper
    return outer_function





username = input("Enter your username: ")
password = input("Enter your password: ")

@admin_only(username, password)
def add_product(product_name):
    print(f"{product_name} added successfully")

product_name = input("Enter product name: ")
add_product(product_name)