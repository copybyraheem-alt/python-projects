class Hero:

    party_gold= 100

    def __init__(self, name):
        self.name= name
        self.health =100

    def take_damage(self, amount):
        future_health= self.health - amount
        if future_health <=0:
            self.health = 0
            return f"{self.name} fainted!"
        else:
            self.health = future_health
            return f"{self.name} took {amount} damage. Health: {self.health}"
        
    def loot(self, amount):
        Hero.party_gold += amount
        return f"{self.name} added {amount} gold to party treasury, Total gold: {Hero.party_gold}"

    def heal(self):
        future_money = Hero.party_gold - 40
        future_health = self.health + 40
        if Hero.party_gold <40:
            return f"Not enough gold!: {Hero.party_gold} available, 40 needed."
        elif Hero.party_gold >=  40:
            if future_health > 100:
                if self.health ==100:
                    return f"you dont need to heal, you are already at {self.health}"
                self.health =100
                Hero.party_gold -= 20
                return f"Your health has been recovered to 100, and used 20 gold, Total gold: {Hero.party_gold}"

            else:
                self.health = future_health
                Hero.party_gold -=40
                return f"{self.name} regained 40 health. Health: {self.health}, Gold: {Hero.party_gold}"

        
dude1=(Hero("dude"))

print(dude1.take_damage(50))
print(dude1.heal())
print(dude1.heal())
print(dude1.heal())



        

        
        

