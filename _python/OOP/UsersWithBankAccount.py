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
    def __init__(self, name, accounts=None):
        self.name = name
        self.accounts = accounts if accounts else {}  


    def UserAccount(self,accountNum):
        self.accounts[accountNum] = BankAccount()

    def make_deposit(self, amount,accountNum):
        self.accounts[accountNum].deposit(amount)

    def make_withdrawal(self, amount,accountNum):
        self.accounts[accountNum].withdraw(amount)

    def display_user_balance(self,accountNum):
        print(f"User:{self.name} Balance:{self.accounts[accountNum].balance}")

user1 = User("Ola")
user1.UserAccount(1)
user1.UserAccount(2)
user1.display_user_balance(1)
user1.display_user_balance(2)
user1.make_deposit(1000,1)

user1.display_user_balance(1)
user1.make_deposit(5000,2)

user1.display_user_balance(2)

user1.make_withdrawal(50,1)
user1.display_user_balance(1)

user1.make_withdrawal(500,2)
user1.display_user_balance(2)

user1.accounts[1].yield_interest()
user1.display_user_balance(1)

user1.accounts[2].yield_interest()
user1.display_user_balance(2)

        
