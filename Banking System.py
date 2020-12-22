class User(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("-------------------")
        print("Account Details")
        print("-------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("You have succesfully made a deposit of $", amount, "your current balance is $", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("You do not have the money to retire $", amount, "your current balance is $", self.balance)
        else:
            self.balance -= amount
            print("You have succesfully made a withdraw of $", amount, "your current balance is $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Your current balance is $", self.balance)
        print("-------------------")

user1 = Bank("Paolo Reyes", 17, "Male")
user1.view_balance()
user1.deposit(100)
user1.withdraw(90)
user1.withdraw(9)
user1.withdraw(10)
user1.view_balance()