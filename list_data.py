# important
# array(list) => collection of data in continuous memory(RAM). It is Abstract data type and we can manipulate it using index (0 to n-1) if you have n data.
# -> it is defined inside big braces [] and value is sperated by comma(,)

fruits = ["apple", "banana", "orange", "papaya", "mango", "kiwi", "watermelon"]
# fruits[0] = "Strawberry"
# print(fruits)

# type
# print(type(fruits))

# length of array
# print(len(fruits))

# accessing value => [start:end:step] => 0, n-1, n-1 => 1
# print(fruits[0])
# print(fruits[-1])
# print(fruits[0:5])
# print(fruits[::2])
# print(fruits[:])

# looping => in, not in
# for fruit in fruits:
#     print(fruit)

# i = 0
# while(i < len(fruits)):
#     print(fruits[i])
#     i+=1


# using while loop
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i+=1

# add
# append(value) => add the value at the end of list
# fruits.append("strawberry")
# print(fruits)

# insert(index, value) => add the value at the given index of the list
# fruits.insert(0, "dragonfruits")
# print(fruits)

# extends(value)=>

# vegetables = []

# veg = ["paneer","cabbage","spinach"]
# non_veg = ["mutton", "buff", "chicken"]

# veg.extend(non_veg)
# print(veg)





# veg = ["cauliflower", "brocoli", "cabbage", "spinach"]
# non_veg = ["fish", "chicken", "pork", "mutton"]

# vegetables = veg + non_veg
# print(vegetables)

# seperate the odd and even number between 1 to 100 in different list
# odd_number = [1,3,...,19]
# even_number = [2,4,6, ..., 20]
# range(20)

# update
# numbers = [1,2,3,4,5,6]

# numbers[0]= "apple"

# print(numbers)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# delete items from the list

# remove(value)
# fruits = ["apple","banana","orange"]
# fruits.remove("strawberry")
# print(fruits)


# print(fruits)

fruits = ["apple","banana","orange"]
item = fruits.pop(1)
print(fruits)
print(item)
# pop(index)
# removed_item = fruits.pop()
# print(fruits)
# print(removed_item)

# clear()
# fruits.clear()
# print(fruits)

# del fruits
# print(fruits)

# sort()
# fruits = ["Apple", "Banana", "cherry", "orange", "kiwi", "mango","apple","orange","apple"]
# fruits.sort(reverse=True)
# print(fruits)

# numbers = [2,3,9,4,0,1]
# numbers.sort(reverse=True)
# print(numbers)
# sorted()

# copy()

# matrix = [
#     # "sachin", "prastut",
#     [1,2,3],
#     [4,5,6],
# ]
# print(matrix)

# for i in matrix: # traverse row
#     for j in i: # traverse column of each row
#         print(j)


# numbers = [1, 9, 7 , 8 ,2 , 4, 5, 0]

# # sort the number except 7 and 9
# sorted_element = []
# other_numbers = []

# for i in numbers:
#     if i == 9 or i == 7:
#         sorted_element.append(i)
#     else:
#         other_numbers.append(i)

# result = sorted_element + sorted(other_numbers)
# del sorted_element
# del other_numbers
# print(result)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8, 9]
# ]

# for row in matrix:
#     # print("row ===> ",row)
#     for col in row:
#         print("data ===> ",col)

