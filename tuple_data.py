# tuple => it is the datatype of python that is immutable(cannot modify once it is created.) => we can create tuple either using () or tuple()

# name = ("Aris","Prastut")

# name[0] = "Sachin"
# print(name)

# my_tuple = (1,2,"mango",4,5,"prastut")
# print(type(my_tuple))
# accessing of the value can be done same like list
# print(my_tuple[0])
# for i in my_tuple:
#     print(i)

# length
# print(len(my_tuple))

# my_tuple[2] = "orange"
# print(my_tuple)

# my_list = list(my_tuple)
# my_list[2] = "orange"
# print(tuple(my_list))

# veg = ("spinach","cauliflower","cabbage","brocauli","cucumber","spinach")
# non_veg = ('chicken','fish','mutton','pork')

# vegetables = veg * 2
# print(vegetables)

# print(veg.count("spinach"))
# print(veg.index("cauliflower"))

# unpacking
# fruits = ("apple","mango","banana","watermelon")

# (a,b,*c )= fruits
# print(a)
# print(b)
# print(c)


# find the odd and even number from 1 to 100 using tuple
# odd_number = (1,3,...)
# even_number = (2,4,...)

# odd_number= []
# even_number = []
# for i in range(1,101):
#     if i % 2 == 0:
#         even_number.append(i)
#     else:
#         odd_number.append(i)

# print(tuple(odd_number))
# print(tuple(even_number))

# fruits = ("mango","banana","orange","papaya","strawberry")

# a,b,*c = fruits
# print(c)

student_info = {
    "name": "Ares",
    "course": "Python",
    "fee": 20000
}

for key,value in student_info.items():
    print(key)
    print(value)