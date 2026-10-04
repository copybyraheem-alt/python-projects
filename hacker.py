class Laptop:

    def __init__(self, brand, os):
        self.brand = brand
        self.os = os
        self.battery = 100

    @property
    def battry(self):
        return self.battery

    @battry.setter
    def battry(self, value):
        self.battery = value

    def write_code(self, hours):
        if hours < 0:
            return "Hours cannot be negative."
        if self.battery <= 0:
            return f"{self.brand} battery is dead! Please charge it first."
        self.battery = max(0, self.battery - hours * 15)
        return f"{self.brand} running {self.os} coded for {hours} hours. Battery is now at {self.battery}%"

    def charge(self):
        self.battery = 100
        return f"{self.brand} laptop is fully charged."


if __name__ == "__main__":
    laptop1 = Laptop("hp victus", "linux")
    laptop2 = Laptop("Mac m3", "Mac os")

    print(laptop1.write_code(2))
    print(laptop1.write_code(3))

    print(laptop2.write_code(1))
