class Wallet:

    def __init__(self, amount):
        self.amount=amount

    def __str__(self):
        return f"Amount ${self.amount:.2f}"

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __sub__(self, other):
        calc= self.amount - other.amount
        if calc < 0:
            raise ValueError ("Insufficient funds")
        else:
            return self.amount - other.amount

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.amount> other.amount:
            return False
        else:
            return True


w1=Wallet(50.5)
w2=Wallet(20.25)

print(w1+w2)
print(w1 - w2)
print(w1 == w2)
print(w1 - w2)

