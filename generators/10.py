class Player:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def show(self):
        print(f"Your name is {self.name}.You're health is {self.health}.")
class Wrrior(Player):
    def __init__(self,name,health,armor):
        super.__init__(name,health)
        self.armor=armor
    def defend(self):
        print(f"{self.name} blocks with armor {self.armor}")