class Account:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance-amount

a = Account(100)
a.deposit(100)
a.withdraw((500))



