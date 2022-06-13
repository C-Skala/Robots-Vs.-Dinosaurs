from weapons_class import Weapon

class Robot:

    def __init__(self, name) -> None:
        self.name = 'ratchet'
        self.health = 100
        self.active_weapon = Weapon()

    def robot_attack(self, dinosaur):
        dinosaur.health -= Weapon.attack_power
        print(f'{self.name} attecked {dinosaur.name} with {Weapon.name} for {Weapon.attack_power}')
        print(f'{dinosaur.name} is now at {dinosaur.health}')