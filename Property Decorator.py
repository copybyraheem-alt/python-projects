class Product:
    def __init__(self,price, quantity):
        if price <0:
            raise ValueError("Price cannot be negative")
        else:
            self.price=price

        if quantity <1:
            raise ValueError("Quantity must be at least 1")
        else:
            self.quantity=quantity



    @property
    def total(self):
        return self.price * self.quantity

    @property
    def discounted_total(self):
        disc= self.total *0.90
        return disc

    @property
    def summary(self):
        return f"{self.quantity} x ${self.price:.2f} = ${self.total:.2f}"


p1=Product(10, 5)
p2=Product(0,1)

print(p1.total)
print(p1.discounted_total)
print(p1.summary)
print(p2.summary)





        
        