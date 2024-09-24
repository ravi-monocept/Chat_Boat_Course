class Enemy:
    def __init__(self, Type_Of_enemy="Zombie", Health_point=10, attack_damage=1):
        self.__Type_Of_enemy = Type_Of_enemy
        self.Health_point = Health_point
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__Type_Of_enemy

    def set_type_of_enemy(self, Type_Of_enemy):
        self.__Type_Of_enemy = Type_Of_enemy

    def talk(self):
        print(f"I am a {self.get_type_of_enemy()}. Be Prepared To Fight!")

    def Walk_Forward(self):
        print(f"{self.get_type_of_enemy()} moves closer to you.")

    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks for {self.attack_damage} damage.")

    def special_attack(self):
        print("Enemy has no special atteck")
