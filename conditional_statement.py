# conditional statement=> if, elif , else

# if => it runs when condition is always true
# elif => if there is more than two condition then we use elif
# else => if true condtion fails then it runs

# syntax
# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of code

# day = "sunday"

# if day == "friday":
#     print("Aaja tw python class hunxa.")
# else:
#     print("Aaja tw bida xa.")

number = int(input("Enter your number: "))

if number > 0:
    print(number, "is positive number")
elif number < 0:
    print(number, "is negative number.")
else:
    print("The number is zero")

# task
# take a three number from user and find the greatest number among them
# take a number from user and find whether the number is odd or even
