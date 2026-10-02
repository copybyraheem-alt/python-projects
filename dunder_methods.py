class Wallet:

    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Wallet balance cannot be negative")
        self.amount = amount

    def __str__(self):
        return f"${self.amount:.2f}"

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        return Wallet(self.amount + other.amount)

    def __sub__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        calc = self.amount - other.amount
        if calc < 0:
            raise ValueError("Insufficient funds")
        return Wallet(calc)

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            return False
        return self.amount == other.amount

    def __lt__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        return self.amount < other.amount


w1=Wallet(50.5)
w2=Wallet(20.25)

print(w1)
print(w1+w2)
print(w1 - w2)
print(w1 == w2)
print(w2<w1)
