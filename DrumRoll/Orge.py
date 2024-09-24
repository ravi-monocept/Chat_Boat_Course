from Enemy import *
import random


class Orge(Enemy):
    def __init__(self, Health_point, attack_damage):
        super().__init__(
            Type_Of_enemy="Orge", Health_point=Health_point, attack_damage=attack_damage
        )

    def talk(self):
        print("orge is slamming hands all around !")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print("Orge gets angry and increases attack by 4.")
