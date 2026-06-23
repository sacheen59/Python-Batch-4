# inheritance => inherit the property and methods from parent class to child class
# type of inheritance:
#     single inheritance
#     multilevel inheritance
#     hybrid inheritance
#     multiple inheritance
#     Hierarchical Inheritance

class HajurBaa:
    def hajurbaa_ko_property(self):
        print("Hajur baa ko property")


class Baba(HajurBaa):

    def baba_ko_property(self):
        print("Baba ko property")


# class Uncle(HajurBaa):
#     def uncle_ko_property(self):
#         print("Uncle ko property")

class Nati(Baba):
    def nati_ko_property(self):
        print("Naati ko property")


# # obj = HajurBaa()
# # obj.hajurbaa_ko_property()
# obj = Nati()
# obj.hajurbaa_ko_property()

# class A:
#     def func_A(self):
#         print("this is function of A")

#     def dispay(self):
#         print("This is display of A")

# class B:
#     def func_B(self):
#         print("This is function of B")

#     def display(self):
#         print("this is display of C")

# class C(B, A):
#     def func_C(self):
#         print("this is function of C.")

# c = C()
# c.dispay()


class NegativeException(Exception):
    def __init__(self, *args):
        super().__init__("The number must not be negative.")


try:
    x = int(input("Enter your number: "))

    if x < 0:
        raise NegativeException()
except NegativeException as e:
    print(e.args[0])
