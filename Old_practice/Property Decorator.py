class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError("Quantity must be at least 1")
        self._quantity = value

    @property
    def total(self):
        return self.price * self.quantity

    @property
    def discounted_total(self):
        return self.total * 0.90

    @property
    def summary(self):
        return f"{self.quantity} x ${self.price:.2f} = ${self.total:.2f}"


if __name__ == "__main__":
    p1 = Product(10, 5)
    p2 = Product(0, 1)

    print(p1.total)
    print(p1.discounted_total)
    print(p1.summary)
    print(p2.summary)
