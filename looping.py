# looping => iteration over a program
# 1. initialization
# 2. condition
# 3. increment/decrement

# while loop
# syntax:
    # while condtion:
    #     program to run
    #     increment/decrement

i = 0 #initialization
# while i < 10: #condition
#     print("hello world")
#     i +=1 #increment

# print(range(10)) => range(start,stop, step) => start = 0(not given), stop=n-1, step = n-1
# for i in range(1,10,2):
#     print(i)
# find the all even number from 1 to 20 using while loop

# j = 10
# while j > 0:
#     print("second hello world")
#     j -= 1

# number = [1,2,3,4,5]

# for i in number:
#     print(i)

# range(start,stop,step) => n-1, n-1
# for i in range(0,100,2):
#     print(i)

# break and continue

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# task
# take the age from user and find whether he or she is valid for citizenship or not
# find the even number from 1 to 100 (without using range)
# find the square of numbers from 1 to 20
# find all multiple of 5 and 3 from 1 to 100


for i in range(10):
    if i == 5:
        continue
    print(i)