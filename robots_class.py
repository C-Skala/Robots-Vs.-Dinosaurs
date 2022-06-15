from weapons_class import Weapon

class Robot:

    def __init__(self) -> None:
        self.name = 'ratchet'
        self.health = 100
        # self.pick_weapon()
        self.active_weapon = Weapon('lazer', 15)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attecked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power}')
        print(f'{dinosaur.name} is now at {dinosaur.health}')

    # def pick_weapon(self):
    #     # logic to pick random weapon
    #     if random_number == 0:
    #         self.active_weapon = Weapon( 'lazer', 15)
    #     pass