from weapons import Weapon
from dinosaurs import Dinosaur  

class Robot:

    def __init__(self) -> None:
        self.name = 'ratchet'
        self.health = 100
        self.active_weapon = Weapon()

    def robot_attack(self):
        print(f'{Robot.name} attaks {Dinosaur.name} with {Weapon.name} for {Weapon.attack_power}')
        Dinosaur.health -= Weapon.attack_power
        print(f'{Dinosaur.name} now has {Dinosaur.health} remaining')