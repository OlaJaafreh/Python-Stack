class BankAccount:
    def __init__(self, interest_rate=0.00, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("No cridit left")
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
        

OlaAccount = BankAccount(0.01,10)
MajedAccount = BankAccount(0.1,10)


OlaAccount.deposit(1000000).deposit(231561).deposit(354621).withdraw(50).display_account_info()
MajedAccount.deposit(50).deposit(100).withdraw(20).withdraw(30).withdraw(40).withdraw(10).yield_interest().display_account_info()
