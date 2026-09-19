class Product:
    inventory=[]
    discount_rate=0.0
    allowed_categories=["Electronics", "Clothing", "Food", "Books"]

    def __init__(self, name, category, price, stock):
        self.name=name
        if category not in Product.allowed_categories:
            raise ValueError("Invalid category")
        else:
            self.category=category

        if price>0:
            self.price= float(price)
        else:
            raise ValueError("Invalid price")     
               
        if stock >=0:
            self.stock=int(stock)
        else:
            raise ValueError("Invalid stock")     

        Product.inventory.append(self)


    def get_discounted_price (self):
        return round(self.price * (1 - Product.discount_rate), 2)

    def sell(self, quantity):
        if quantity>0 and quantity <= self.stock:
            self.stock-=quantity
            return True
        else:
            return False

    @classmethod
    def from_csv(cls, csv_string):
        formatted=csv_string
        Name,Category,Price,Stock= formatted.split (",")
        Name = Name.strip()
        Category = Category.strip()
        Price = float(Price.strip())
        Stock = int(Stock.strip())
        return cls(Name,Category,Price,Stock)

    @classmethod
    def from_dict(cls, data):
        return cls((data["name"]), (data["category"]), (data["price"]), (data["stock"]))

    @classmethod
    def set_discount_rate(cls, rate):
        if rate >=0 and rate <=0.90:
            final_rate= Product.discount_rate =rate
            return final_rate
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
        for item  in cls.inventory:
            if item.category == category:
                matching_names.append(item.name)
        return matching_names


p1=Product("Python Basic","Books", 29, 20 )
p2=Product.from_csv("Wireless Mouse, Electronics , 25.00 , 50")
p3=Product.from_dict({"name": "Jeans", "category": "Clothing", "price": 45.0, "stock": 10})

Product.total_inventory_value()
Product.set_discount_rate(0.15)
print(p1.get_discounted_price())
print(p2.sell(5))
print(p2.stock)
print(Product.find_by_category("Electronics"))

try:
    invalid_p = Product("Bad Item", "Toys", 10.0, 5)
except ValueError as e:
    print(f"Caught expected error: {e}")