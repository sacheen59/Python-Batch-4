# ADT => Abstract Data Type => Array => index => 0 to n-1
# CRUD => Create, Read, Update, Delete

# Mutable => which data can be changed (modify) [list, dictionary, set]
# Immutable => whose data cannot be modified [string, tuple]

# name = "Ares" # name = 'A', 'r', 'e', 's'

name = "Dipesh"

# print(len(name))

# length
# print(len(name))

# # looping
# for i in name:
#     print(i)

# accessing or slicing
# print(name[0])

# slicing the character
# name[start: stop: step] stop > start=> stop => n-1, step => n-1
# print(name[0])
# print(name[2])
# text = "We are learning python"
# print(text[0:10:2])
# print(text[-4:])
# print(text[::-1])
# text= "we are learning python"

# print(text[1:10])
# print(text[1:])
# print(text[:9])
# print(text[:])
# print(text[::2])
# print(text[-1])
# print(text[-5:])

# # string methods
# text = "we are learning string"
# print(text.upper())

# name = "ARES GIRI"
# # print(name.lower())
# # print(name.capitalize())
# print(name.title())

# text= "*******we are learning python. python is best language.####"
# text = "we are learning python. python is best programming language."
# print(text.replace("python","Django"))
# print(text.count("e"))
# print(text.strip("*"))
# print(text.lstrip("*"))
# print(text.rstrip("*"))
# print(text.lstrip("*").rstrip("#"))

# print("Ares" + "Giri")

# print("Ares" * 3)

# txt = "Hi Sam!"

# x = "mSa"
# y = "eJo"

# mytable = str.maketrans(x, y)

# print(txt.translate(mytable))

# def modify_strings(*args):
#     for name in args:
#         print(name.upper())


# modify_strings("dipesh","simran","aaditya")




# email = "sachinbarali@example.com"
# splitted_email = email.split("@")
# # print(splitted_email)
# print("@".join(splitted_email))

# text = "we are learning python. python is best programming language."
# print(text.replace("python","Django",1))

# email = "staff@gmail.com"
# print(email.startswith("staff"))
# print(email.endswith(".com"))
# names = ["dipesh","aaditya","simran"]
# print("**".join(names))

# task
# find whether the given domain name of an user is secure or not (https://www.facebook.com)

valid_domain_suffix = ["com", "in", "io"]
domain = input("Enter your domain: ")

if domain.lower().startswith("https") and domain.split(".")[-1] in valid_domain_suffix:
    print("secure and valid domain")
else:
    print("Invalid domain")



