# Exception Handling(Error Handling) => Handling error so that system cannot crash but give some meaningful message

# try => this is the block of code which you want to try. if all the code is succeed then it finishes the execution
# except => if try blocks fail then, except blocks run
# raise => it is use to raise custom error message
# finally => finally runs whether the program have error or not.
# else =>

# try:
#     first_number = int(input("Enter your first number: "))
#     second_number = int(input("Enter your second number: "))
#     division = first_number / second_number
#     print(division)
# except (ZeroDivisionError,ValueError) as e:
#     print({"error_message": e.args[0]})
# except ValueError as e:
#     print({"error_message": e.args[0]})
# except:
#     print("Something went wrong")
# finally:
#     print("Division program ended.")


# suppose four student came at devsign for python django course inquiry in a batch. Dependra sir gave certain amount of discount to each student. find the total revenue of the devsign from this batch in first installment, second installment and final revenue. You have following data to manipulate:

# students = [
#     {
#         "id": 'pd1',
#         "name": 'Aaditya',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "10%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd2',
#         "name": 'Prastut',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "8%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd3',
#         "name": 'Upadesh',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "12%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd4',
#         "name": 'Simran',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "15%",
#         "registration_fee": "Rs. 2500"
#     },

# ]

# first installment ===> Rs. ...
# second installment ===> Rs....
# final revenue ===> Rs ....


# students = [
#     {
#         "id": 'pd1',
#         "name": 'Aaditya',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "10%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd2',
#         "name": 'Prastut',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "8%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd3',
#         "name": 'Upadesh',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "12%",
#         "registration_fee": "Rs. 2500"
#     },
#     {
#         "id": 'pd4',
#         "name": 'Simran',
#         "course": 'Python with Django',
#         "price": "Rs. 25000",
#         "discount": "15%",
#         "registration_fee": "Rs. 2500"
#     },
# ]

# def convert_to_number(price):
#     p = price.split(" ")[1]
#     return int(p)

# def percentage_to_number(percent_data):
#     original_data = percent_data.strip("%")
#     return float(original_data)


# first_installment = 0
# second_installment = 0
# for student in students:
#     name = student["name"]
#     course_price = convert_to_number(student["price"])
#     discount_rate = percentage_to_number(student["discount"])
#     registration_fee = convert_to_number(student["registration_fee"])
#     fee_except_registration = course_price - registration_fee
#     course_price_after_discount = fee_except_registration - (fee_except_registration * (discount_rate / 100))
#     installment = course_price_after_discount / 2
#     first_installment += installment
#     second_installment += installment
#     print("first_installment ===> ",(name, first_installment))
#     print("second_installment ===> ",(name, second_installment))

# total = first_installment + second_installment
# print("total====>",total)


# first_installment = sum(installments)
# second_installment = sum(installments)
# final_installment = first_installment + second_installment
# print(final_installment)


# age = int(input("Enter your age: "))

# try:
#     if age < 16:
#         raise Exception("The age must not be greater than 16.")
# except Exception as e:
#     print(e.args[0])
# else:
#     print("You are valid for citizenship.")


# class NegativeNumberException(Exception):
#     def __init__(self):
#         super().__init__("Number must be greater than 0.")

# number = int(input("Enter your number: "))

# try:
#     if number < 0:
#         raise NegativeNumberException()
# except NegativeNumberException as e:
#     print(e.args[0])
# else:
#     print(number)


# try:
#     first_number = int(input("Enter your first number: "))
#     second_number = int(input("Enter your second number: "))

#     division = first_number / second_number

# except ZeroDivisionError:
#     print("The second number must not be zero.")
# except ValueError:
#     print("The number must be interger.")
# else:
#     print(f"division of number is {division}")

# finally:
#     print("This runs either try block succeed or failed.")
