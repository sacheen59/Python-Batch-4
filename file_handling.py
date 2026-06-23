# file handling is the process of handling file operations like write, read to store and manipulate the data. Type of files may be .txt,.json, .csv, .xls

# 1. open the file
# 2. manupulate the file or do file operations
# 3. close the file

# there are different mode to open the file => read(r), write(w), append(a), create(x)
# read => to read the content of the file we open file in read mode. If file doesnot exists it will throw an error
# write => to write the content in the file but whenever we write the content on the same file again the previous content will be lost. If file doesnot exists it will create a new file
# append => same as write mode but it doesn't overwrite but add the content to the previous content


# read mode
# file = None
# try:
#     file = open("student.txt","r")
#     for data in file:
#         print(data.split(":")[1].strip("\n"))
#     # splitted_content = content.split("\n")
#     # for i in splitted_content:
#     #     print(i.split(":")[1])
#     # for data in content:
#     #     print(data.split(":")[1])
# except FileNotFoundError as e:
#     print(f"error ==> {e.args[1]}")
# finally:
#     if file:
#         file.close()

# file = open("./student.txt","r")
# content = file.readlines()
# print(type(content))
# print(content)
# file.close()


# file_paths= ["student.txt","student_info.txt"]

# for path in file_paths:
#     print("Name of file: ",path)
#     with open(f"{path}","r") as file:
#         content = file.read()
#         print(content)

# with open("test.txt","a+") as file:
#     old_content = file.read()

#     # 2. Move the cursor back to the absolute beginning
#     file.seek(0)

#     # 3. Write your new text
#     file.write("This is the new first line.\n")

#     # 4. Append the old content right after it
#     file.write(old_content)


# with open("student.txt","r") as file:
#     content = file.read()
#     print(content)


contents = [
    "this is python class.\n",
    "we are learning python.\n",
    "python is the best programming language.\n"
]

with open("test.txt","w") as file:
    file.writelines(contents)
    print("file wrote successfully.")

# student_info = []

# for i in range(2):
#     name = input("Enter your name: ")
#     course = input("Enter your course: ")
#     student_info.append(f"Name: {name} ===> Course: {course}\n")

# print(student_info)
# with open("./student/student_info.txt","a") as f:
#     f.writelines(student_info)


# data entry software
# enter name, address and contact number of the student