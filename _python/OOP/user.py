class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print("No cridit left")
            print(f"No cridit left ----> Your Balance is: {self.balance}")
            return
        self.balance -= amount


    def display_user_balance(self):
        print(f"User:{self.name} Balance:{self.balance}")

    def transfer_money(self, OtherUser, amount):
        self.make_withdrawal(amount)
        OtherUser.make_deposit(amount)

user1 = User("Ola")
user2 = User("Saed")
user3 = User("Majed")


user1.make_deposit(50000000)
user1.make_deposit(600000)
user1.make_deposit(70000)
user1.make_withdrawal(5)

user1.display_user_balance()


user2.make_deposit(100)
user2.make_deposit(200)
user2.make_withdrawal(200)
user2.make_withdrawal(50)

user2.display_user_balance()


user3.make_deposit(1000)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.make_withdrawal(60)

user3.display_user_balance()

user1.transfer_money(user3, 50000)

user1.display_user_balance()
user3.display_user_balance()
