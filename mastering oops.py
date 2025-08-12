class Player:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def display_info(self):
        print(f"Player - {self.name}, Health = {self.health}, Attack Power = {self.attack_power}")
    def take_damage(self,damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health is now {self.health}")
player_one = Player("Snow",100,70)
player_one.display_info()
player_one.take_damage(40)
player_one.display_info()

