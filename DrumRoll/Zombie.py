from Enemy import *
import random


class Zombie(Enemy):
    def __init__(self, Health_point, attack_damage):
        super().__init__(
            Type_Of_enemy="Zombie",
            Health_point=Health_point,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("Grumbling __--!")

    def spread_disease(self):
        print("zombie is trying to spread Desiese !")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.Health_point += 2
            print("Zombie regenerated 2HP!")
