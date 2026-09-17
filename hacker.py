class Laptop:


    def __init__(self, brand, os,):
        self.brand=brand
        self.os=os
        self.battry= 100

    def write_code(self, hours):
        self.battry -= hours*15
        return f"{self.brand} running {self.os} coded for {hours} hours. battrey is now at {self.battry}%"

    def charge(self):
        self.battry=100
        return f"laptop is fully charged"

laptop1= Laptop("hp victus", "linux")
laptop2= Laptop("Mac m3", "Mac os")

print(laptop1.write_code(2))
print(laptop1.write_code(3))

print(laptop2.write_code(1))


