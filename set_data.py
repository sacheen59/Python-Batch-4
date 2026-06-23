# set => unordered collection of data and not duplicated

# my_set = {10,1,2,3,4,5,6,6,7,8,8}
# print(type(my_set))
# print(my_set)
# print(my_set)

names = {"Aaditya", "Upadesh", "Simran", "Prastut"}
# print(names)

# for i in names:
#     print(i)

# names.add("Amit")
# print(names)
# names.remove("Simran")
# print(names)


A = {1,2,3,4,5}
B = {2,3,4,5,6}

# result = A.union(B)
# result = A | B
# print(result)

# intersection => common item between two set
# intersection_result = A.intersection(B)
# intersection_result = A & B
# print(intersection_result)

# C = {1,2,3}
# D = {0,1,2,3,4}
# is_subset = C.issubset(D)
# print(is_subset)

# print(D.difference(C))
# print(D - C)

thisset = {"apple", "banana", "cherry"}
# thisset.remove("pineapple")
thisset.discard("pineapple")
print(thisset)

# A = {1,2,3,4,5}
# B = {6,7,8}

# print(A.isdisjoint(B))

numbers = [1,2,3,4,4,5,6,7,7]
result = set(numbers)
print(list(result))
