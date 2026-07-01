# dictionary => it is the data structure in python which comes with key value pair.
# we can define dictionary using {} or dict()
# syntax
# dictionary_name = {
#     key1: value1,
#     key2: value2,
#     key3: value3,

#     keyn: valuen,
# }

# student_info = {
#     "name": "Ares Giri",
#     "course": "Python with Django",
#     "fee": 20000
# }

# student_info = dict(name="Ares Giri", course="Python with Django",fee=20000)

# print(type(student_info))

# print(student_info["name"])
# print(student_info["fee"])

# student_info["fee"] = 40000
# student_info["age"] = 20
# print(student_info)

# print(len(student_info))

# looping => keys(), items(), values()
# for data in student_info.items():
#     print(data)

# student_info = dict(name="Sachin")
# print(student_info)

# student_info = {
#     "name": "Prastut",
#     "course": "python with Django",
#     "marks": [20,30,40,50],
#     "subject": {
#         "english": 20,
#         "math": 90
#     }
# }
# length of dict
# print(len(student_info))

# accessing
# print(student_info["name"])


# .values => it is use to access the values of dictionary using loop
# .keys => it is use to access the keys of dictionary using loop
# .items => it is use to access the keys and value of dictionary using loop. It returns the data in tuple

# changing the item of the dictionary
# student_info = {
#     "name": "Prastut",
#     "age": 23,
#     "course": "python",
#     # "fee":20000
# }

# access
# .get()
# print(student_info.get("fee", 30000))
student_info = {
    "name": "Ares Giri",
    "course": "Python with Django",
    "fee": 20000,
}

# name_of_student = student_info.pop("duration",3.5)
# print(name_of_student)
# print(student_info)
# student_info["duration"]

# print(student_info.get("duration",3.5))

# update() => use to update the key value pair in the existing dict
# student_info.update({
#     "duration": "3.5 Months"
# })
# print(student_info)
# student_info.update(
#     {
#         "name": "simran",
#         "duration": "3.5 months",
#         "fees": 20000
#     }
# )
# print(student_info)

# pop() => this is use to remove the item using specific key
# course = student_info.pop("duration",3.5)
# print(student_info)
# print(course)

# popitem()
item = student_info.popitem()
print(student_info)
# print(item)

# first_student = {
#     "name": "Prastut",
#     "age": 23,
#     "course": {
#         "course_name": "python",
# 	    "duration": 3.5,
#         "price": 22500,
# 	}
# }

# for key,value in first_student.items():
#     # if key == "course":
#     #     print(value["course_name"])
#     print(value)
#     if type(value) == dict:
#         print(value["course_name"])

# name = ('Simarn','Aaditya', 'Upadesh', 'Prastut')
# fruits = ('Watermelon', 'Mango', 'Orange', 'Apple')

# student_info = {
#     "name": "Prastut",
#     "course": "python with Django",
#     "marks": [20,30,40,50]
# }

# marks = student_info["marks"]
# total_marks = sum(marks)
# print(total_marks)

# student_info = [
#     {
#         "name": "Ram",
#         "marks": {
#             "math": 90,
#             "social": 20,
#             "english": 40,
#         }
#     },
#     {
#         "name": "Hari",
#         "marks": {
#             "math": 85,
#             "social": 45,
#             "english": 35,
#         }
#     },
#     {
#         "name": "Geeta",
#         "marks": {
#             "math": 55,
#             "social": 58,
#             "english": 29,
#         }
#     },
#     {
#         "name": "Sita",
#         "marks": {
#             "math": 56,
#             "social": 86,
#             "english": 49,
#         }
#     },
# ]
# - from the given data find which student got the highest marks with his/her name.
# - find the highest marks of a subject with subject name



# carts = [
#     {
#         "item": {
#         "id": 1,
#         "product_name": "mobile phone",
#         "price": 2000
#         },
#         "quantity": 3
#     },
#     {
#         "item" :{
#         "id": 1,
#         "product_name": "watch",
#         "price": 1000
#         },
#         "quantity": 2
#     },
#     {
#         "item" : {
#         "id": 1,
#         "product_name": "airpods",
#         "price": 3000
#         },
#         "quantity": 1
#     },
#     {
#        "item": { "id": 1,
#         "product_name": "lapotp",
#         "price": 100000
#         },
#         "quantity": 2
#     },
# ]

# find the total price that user need to pay during checkout

# mobile ===> total price
# watch ===> total price
# airpods ===> total price
# laptop ====> total price
# =========================
# Total ======> overall total






# name = ('Simarn','Aaditya', 'Upadesh', 'Prastut')
# fruits = ('Watermelon', 'Mango', 'Orange', 'Apple')

# fav_veg = zip(name,fruits)
# print(dict(fav_veg))
