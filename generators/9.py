class Player:
    def __init__(self,name,health,damage):
        self.name=name
        self.health=health
        self.damage=damage
    def atack(self,other_player):
        other_player.health-=self.damage
        if other_player.health<=0:
            print(f"{other_player.name} is dead")
        else:
            print(self.name ,"attacked", other_player.name)
            print(other_player.name,"health:",other_player.health)
    def show(self):
        print("Your health: ",self.health)
player1=Player("Black",100,25)
player2=Player("White",110,20)
player2.atack(player1)


