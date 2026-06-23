# filter => higher order function that return the items in list which matches the condtion
# function and iterator as an argument

names = ["ares","aaditya","dipesh","simran"]

# def start_a(name):
#     return name.startswith("a")
# output = []
# for i in names:
#     if i.startswith("a"):
#         output.append(i)

# print(output)

# # ["ares","aaditya"]
# result = list(filter(lambda x: x.startswith("a"), names))
# print(result)


# filter the item from 1 to 20 i.e multiple of 3 and 5

# zip
# names = ["ares", "aaditya","simran","dipesh"]
# fav_fruits = ["apple","kiwi","mango","strawberry"]
# print(list(zip(names,fav_fruits)))

# enumerate
names = ["ares", "aaditya","simran","dipesh"]
# 0 ares
# 1 aaditya

# for index in range(len(names)): #range(0,4) names[0]
#     print(index, names[index])

# for index, value in enumerate(names):
#     print(index,value)

my_text = ["flower","flawn","flow", "flown"]
# output => "fl"


