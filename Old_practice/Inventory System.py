class Product:
    inventory = []
    discount_rate = 0.0
    allowed_categories = ["Electronics", "Clothing", "Food", "Books"]

    def __init__(self, name, category, price, stock):
        self.name = name
        if category not in self.allowed_categories:
            raise ValueError("Invalid category")
        self.category = category

        if price > 0:
            self.price = float(price)
        else:
            raise ValueError("Invalid price")

        if stock >= 0:
            self.stock = int(stock)
        else:
            raise ValueError("Invalid stock")

        self.inventory.append(self)

    def get_discounted_price(self):
        return round(self.price * (1 - self.discount_rate), 2)

    def sell(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0 or quantity > self.stock:
            return False
        self.stock -= quantity
        return True

    @classmethod
    def from_csv(cls, csv_string):
        parts = csv_string.split(",")
        if len(parts) != 4:
            raise ValueError("CSV string must have 4 comma-separated values (Name, Category, Price, Stock)")
        name = parts[0].strip()
        category = parts[1].strip()
        price = float(parts[2].strip())
        stock = int(parts[3].strip())
        return cls(name, category, price, stock)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["category"], data["price"], data["stock"])

    @classmethod
    def set_discount_rate(cls, rate):
        if 0.0 <= rate <= 0.90:
            cls.discount_rate = rate
            return cls.discount_rate
        else:
            raise ValueError("Discount must be between 0.0 and 0.90")

    @classmethod
    def total_inventory_value(cls):
        total = 0
        for item in cls.inventory:
            total += item.price * item.stock
        return total

    @classmethod
    def find_by_category(cls, category):
        matching_names = []
        for item in cls.inventory:
            if item.category == category:
                matching_names.append(item.name)
        return matching_names


if __name__ == "__main__":
    p1 = Product("Python Basic", "Books", 29, 20)
    p2 = Product.from_csv("Wireless Mouse, Electronics , 25.00 , 50")
    p3 = Product.from_dict({"name": "Jeans", "category": "Clothing", "price": 45.0, "stock": 10})

    print(f"Total inventory value: {Product.total_inventory_value():.2f}")
    Product.set_discount_rate(0.15)
    print(p1.get_discounted_price())
    print(p2.sell(5))
    print(p2.stock)
    print(Product.find_by_category("Electronics"))

    try:
        invalid_p = Product("Bad Item", "Toys", 10.0, 5)
    except ValueError as e:
        print(f"Caught expected error: {e}")
