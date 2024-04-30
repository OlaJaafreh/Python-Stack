class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print("No cridit left")
            print(f"No cridit left ----> Your Balance is: {self.balance}")
            return
        self.balance -= amount
        return self


    def display_user_balance(self):
        print(f"User:{self.name} Balance:{self.balance}")
        return self

    def transfer_money(self, OtherUser, amount):
        self.make_withdrawal(amount)
        OtherUser.make_deposit(amount)
        return self

user1 = User("Ola")
user2 = User("Saed")
user3 = User("Majed")


user1.make_deposit(50000000).make_deposit(600000).make_deposit(70000).make_withdrawal(5).display_user_balance()
user2.make_deposit(100).make_deposit(200).make_withdrawal(200).make_withdrawal(50).display_user_balance()
user3.make_deposit(1000).make_withdrawal(20).make_withdrawal(20).make_withdrawal(60).display_user_balance()

user1.transfer_money(user3, 50000).display_user_balance()
user3.display_user_balance()
