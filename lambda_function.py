# lambda function => it is an anonymous function or shorthand function (if there is only one return statement)

# def square_of_number(num):
#     return num ** 2

# result = square_of_number(10)
# print(result)

# result  = lambda num : num ** 2
# print(result(10))

# # write a lambda function to convert the any text into lower case

# output = lambda text : text.lower()
# print(output("ARES"))

students = [
    {
        "name": "Aaditya",
        "age" : 20,
    },
    {
            "name": "Simran",
            "age" : 30,
        },
    {
            "name": "Upadesh",
            "age" : 10,
        },
        {
                "name": "Ares",
                "age" : 26,
            },
]

# def sorting_key(data):
#     return data["age"]

# students.sort(key=lambda data: data["age"])

# print(students)


# write a function to find the sum of two numbers using lambda function

# sum_of_two_number = lambda x, y : x + y
# print(sum_of_two_number(10,20))

# numbers = [1,2,3,4,5]

# def square(num):
#     return num ** 2

# result = map(lambda x: x ** 2, numbers)
# print(list(result))

# numbers = [1,2,3,4,5]

# def func(num):
#     if num % 2 == 0:
#         return num * 2
#     return num

# # result = list(map(func, numbers))
# result = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
# print(result)

# filter()

# number = int(input("Enter your number: "))

# if number < 0:
#     print("Negative")
# else:
#     if number > 0:
#         print("Positive")
#     else:
#         print("Zero")

numbers = [1,2,3,0,-4,4,5,0,10,-10,-2]
# output = ["postive",..., "Zero", "negative"] using list comprehension

# result = lambda x : "Negative" if x < 0 else "Positive" if x > 0 else "Zero"
# print(result(number))

# result = ["positive" if i > 0 else "negative" if i < 0 else "zero" for i in numbers]
# print(result)