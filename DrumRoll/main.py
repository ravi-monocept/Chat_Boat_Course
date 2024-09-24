from Zombie import *
from Orge import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.Health_point > 0 and e2.Health_point > 0:
        print("-----------------")
        e1.special_attack()
        e2.special_attack()

        print(f"{e1.get_type_of_enemy()} : { e1.Health_point} HPP left !")
        print(f"{e2.get_type_of_enemy()} : { e2.Health_point} HPP left !")

        e2.attack()
        e1.Health_point -= e2.attack_damage
        e1.attack()
        e2.Health_point -= e1.attack_damage

    print("---------------")

    if e1.Health_point > 0:
        print(f"{e1.get_type_of_enemy()} wins !")
    elif e2.Health_point > 0:
        print(f"{e2.get_type_of_enemy()} wins !")


zombie = Zombie(30, 1)
ogre = Orge(30, 1)
battle(zombie, ogre)
