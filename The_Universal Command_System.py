class Robot:
    def walk(self, direction):
        return f"Robot moves: {direction}"
    def move(self, direction):
        return self.walk(direction)
    def hover(self):
        return "Robot ties to hover, but robot can't"

class Drone:
    def fly(self, direction):
        return f"Drone moves: {direction}"
    def move(self, direction):
        return self.fly(direction)
    def hover(self):
        return "The drone hovers"

class SmartCar:
    def drive(self, direction):
        return f"The car moves: {direction}"
    def move(self, direction):
        return self.drive(direction)
    def hover(self):
        return "SmartCar ties to hover, but smartar can't"

objs= [Robot(), Drone(), SmartCar()]

def send_command(machine, direction):
    print("-----------------------")
    print(machine.move(direction))
    print("-----------------------")

def send_advanced_command(machine, direction):
    print("-----------------------")
    print(machine.move(direction))
    print(machine.hover())
    print("-----------------------")


for obj in objs:
    send_command(obj, "Forward")

for obj in objs:
    send_advanced_command(obj, "Back")