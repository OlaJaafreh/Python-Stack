class BankAccount:
    def __init__(self, interest_rate=0.00, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"No cridit left ----> Your Balance is: {self.balance}")
        return self 
        self.balance -= amount
        return self 


    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self 


    def yield_interest(self):
        self.balance  = (self.interest_rate * self.balance) + self.balance
        return self 
        
class User:
    def __init__(self, name ,account=None):
        self.name = name
        self.account = account#List

    def UserAccount(self,accountNum ,balance=0):
        self.account[accountNum] = BankAccount(balance)

    def make_deposit(self, amount,accountNum):
        self.account[accountNum].deposit(amount)

    def make_withdrawal(self, amount,accountNum):
        self.account[accountNum].withdraw(amount)


    def display_user_balance(self):
        print(f"User:{self.name} Balance:{self.account[accountNum].balance}")

user1 = User("Ola")
user1.UserAccount(1,500)


        
