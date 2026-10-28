class Robot:
    def walk(self, direction):
        return f"Robot moves: {direction}"
    def move(self, direction):
        return self.walk(direction)
    def hover(self):
        return "Robot tries to hover, but robot can't"

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
        return "SmartCar tries to hover, but SmartCar can't"

def send_command(machine, direction):
    print("-----------------------")
    print(machine.move(direction))
    print("-----------------------")

def send_advanced_command(machine, direction):
    print("-----------------------")
    print(machine.move(direction))
    print(machine.hover())
    print("-----------------------")

if __name__ == "__main__":
    objs = [Robot(), Drone(), SmartCar()]

    for obj in objs:
        send_command(obj, "Forward")

    for obj in objs:
        send_advanced_command(obj, "Back")
