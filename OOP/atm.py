# Atm app

class Atm:
    def __init__(self):
        self.__pin = 0000
        self.__balance = 0
        self.menu()
    
    def menu(self):
        user_input = int(input("""
                               Enter 1 to set pin :- 
                               Enter 2 to check balance :- 
                               Enter 3 to withdrawl :- 
                               Enter 4 to deposit :- 
                               Enter 5 to exit :- 
                               Default pin is 0000 """))
        if user_input == 1:
            self.setPin()
        elif user_input == 2:
            self.check_balance()
        elif user_input == 3:
            self.withdrawl()
        elif user_input == 4:
            self.deposit()
        else:
            print("Thankyou")
        
    def setPin(self):
        password = int(input("Enter your pin :- "))
        self.__pin += password
        print("your pin set successfully")
        print(self.__pin)

    def check_balance(self):
        passCheck = int(input("Enter pin to continue :- "))
        if passCheck == self.__pin:
            print(f"Your balance is {self.__balance}")
        else:
            print("Invalid request !!!")

    def withdrawl(self):
        passCheck = int(input("Enter pin to continue :- "))
        if passCheck == self.__pin:
            balance = int(input("Enter amount to withdrawl :- "))
            self.__balance = self.__balance - balance
            print("withdrawl successfull")
        else:
            print("Invalid request !!!")

    def deposit(self):
        passCheck = int(input("Enter pin to continue :- "))
        if passCheck == self.__pin:
            balance = int(input("Enter amount to deposit :- "))
            self.__balance = self.__balance + balance
            print("deposti successfull")
        else:
            print("Invalid request !!!")

        