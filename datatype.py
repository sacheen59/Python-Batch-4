# datatype => type of data that is stored in memory address
# there are two types of datatype
# basic data type => int, float, string, boolean, nonetype
# collection or sequence data type => list, dictionary, tuple, set

# basic data type
# int => positive or negative whole number
# x = -10
# print(type(x))

# float => positive or negative number with decimal
# y = 21.2
# print(type(y))

# string => any character that is written inside " " or ' '
# name = "Aris Giri"
# # multiline string =>
# poem = """
# Twinkle Twinkle little star
# how i wonder what you are
# """
# print(poem)

# # boolean => True or False (1, 0)
# is_active = False
# print(type(is_active))

# # None
# a = None

# a = "sachin barali"

# write a program to find the sum between two numbers (Note: Take two number as user input)

# first_number = int(input("Enter your first number: "))
# print(type(first_number))
# second_number = int(input("Enter your second number: "))
# sum = first_number + second_number
# print(sum)

# print("Hello world")
# print(10 + 5)
# print(True)
# print(None)


# maketrans
# text = "Hi Ares HH"
# x = "Hi"
# y = "Be"

# result = text.maketrans(x,y)
# print(result)
# print(text.translate(result))

# try:
#     first = int(input("Enter your first number: "))
#     second = int(input("Enter your second number: "))
#     division = first / second
# except ZeroDivisionError as e:
#     print("Your second number must not be zero.")
# else:
#     print(f"Division is {division}")
# finally:
#     print("this run all the time")

# try:
#     with open("simran.txt","r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError as e:
#     print(e.args[1])

# new_text = "We are learning python\n"

# with open("example.txt", "r+") as file:
#     old_content = file.read()      # Read existing content
#     file.seek(0)                   # Move to the beginning
#     file.write(new_text + old_content)


# type conversion => process of converting one datatype into another data type
# a = str(10.0)
# print(type(a))

# take the user input and find the sum between two numbers
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
add = first_number + second_number
print(add)


