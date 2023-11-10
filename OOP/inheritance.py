# class User:
#     def name(self):
#         print("name")
#     def age(self):
#         print("age")


# class Student(User):
#     def roll(self):
#         print("roll")
#     def marks(self):
#         print("marks")

# test = User()
# test1 = Student()
# test.name()
# test1.age()
# test1.marks()

# no private member will be access in inheritance and super() keyword

class Phone:
    def __init__(self,name,price):
        self.__name = name
        self.price = price
    def buy(self):
        print("Buying phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying Smartphone")
        super().buy()



x = SmartPhone("Apple",2000)

print(x.price)
# print(x.__name)
x.buy()


