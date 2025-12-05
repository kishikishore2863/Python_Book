#A Wallet class stores currency as a class variable.
# Each wallet object stores owner and amount.
# A class method updates currency for all wallets.
# A static method checks if amount is nonnegative.
# Confirm the new currency value for each wallet.


class Wallet:
    currency = "USD"

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    @classmethod
    def update_currency(cls, new_currency):
        cls.currency = new_currency

    @staticmethod
    def is_valid_amount(a):
        return a >= 0

w1 = Wallet("Kishore", 150)
w2 = Wallet("Amit", 300)
w3 = Wallet("Rita", 0)

print(w1.owner, w1.amount, Wallet.currency, Wallet.is_valid_amount(w1.amount))
print(w2.owner, w2.amount, Wallet.currency, Wallet.is_valid_amount(w2.amount))
print(w3.owner, w3.amount, Wallet.currency, Wallet.is_valid_amount(w3.amount))

Wallet.update_currency("INR")

print(w1.owner, w1.amount, Wallet.currency)
print(w2.owner, w2.amount, Wallet.currency)
print(w3.owner, w3.amount, Wallet.currency)