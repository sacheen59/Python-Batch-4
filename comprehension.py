# comprehension => It is the shortcut method to create the collection

# list comprehension
# odd_num = []
# even_num = []

# for i in range(1,100):
#     if i % 2 == 0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)

# print(odd_num)
# print(even_num)

# even_num = [i for i in range(1,20)]
# print(even_num)

# even_num = []

# for i in range(1,20):
#     if i % 2 == 0:
#         even_num.append(i)
# print(even_num)

# syntax
# when there is only if condition
# output = [ reference for reference in collection if condition ]


names = ["ares", "simran", "aaditya","upadesh"]

# result = [name.upper() for name in names if name.startswith('a') ]
# print(result)

# syntax
# when there is if and else condition
# output = [result_of_if if expression else result_of_else for reference in collection]
result = [name.upper() if name.startswith("a") else name.title() for name in names]
print(result)

numbers = [1,2,3,4,5,6,7]
# odd number => square, even_number => multiply by 5 using list comprehension

result = [number ** 2 if number % 2 != 0 else number * 5 for number in numbers]
# output = []
# for number in numbers:
#     if number % 2 == 0:
#         output.append(number * 5)
#     else:
#         output.append(number ** 2)
# print(output)
print(result)

# dictionary comprehesion
x = [1,2,3,4,5]

output = {
    i : i**2
    for i in x
    if i % 2 == 0
}
print(output)

students = ['ares',"aaditya","simran"]
# using dictionary comprehension
# {
#     "a": "ares",
#     "a": "aaditya",
#     "s": "simran"
# }

result_dict = {
    student[0:3]: student
    for student in students
}
print(result_dict)