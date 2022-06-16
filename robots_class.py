from pickle import TRUE
from random import randint
from weapons_class import Weapon

class Robot:

    def __init__(self) -> None:
        self.name = 'ratchet'
        self.health = randint(90, 110)
        
        

    def attack(self, dinosaur):
        weapon_attack = self.pick_weapon()
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power}')
        print(f'{dinosaur.name} is now at {dinosaur.health}')
        print("")

    def pick_weapon(self):
        weapon_picked = False
        while weapon_picked == False:
            weapon_picker = input('please select a number for a weapon: 1-Lazer, 2-Fist, 3-Big Bertha: ')
            if weapon_picker == '1':
                self.active_weapon = Weapon( 'lazer', randint(15,25))
                weapon_picked = True
            elif weapon_picker == '2':
                self.active_weapon = Weapon('Fist', 20)
                weapon_picked = True
            elif weapon_picker == '3':
                self.active_weapon = Weapon('Big Berhta', randint(1, 99))
                weapon_picked = True
            else:
                print('please type either 1, 2, or 3')