# Simple game with classes
# Use health, damage, name, and maybe implement defence and potions and what not, first keep it simple

# Create class
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        

def game_start(Player):
    name = input("What is your name? ")
    
    # Assign Attributes 
    Player.name = name
    Player.health = 10
    Player.damage = 3
    
    print(f"Welcome {Player.name}! Your strength is: {Player.damage} and your health is: {Player.health}. Let's begin your adventure into Middle Earth!")
    # print(Player.name)
    # print(Player.health)
    # print(Player.damage)
    
game_start(Player)
    
    