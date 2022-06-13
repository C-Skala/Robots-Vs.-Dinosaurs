

class Dinosaur:

    def __init__(self, name, attack_power) -> None:
        self.name = 'bones'
        self.attack_power = 20
        self.health = 100

    def Dinosaur_attack(self, robot):
        print(f'{Dinosaur.name} attaks {robot.name} with its powerfull jaws for {Dinosaur.attack_power}')
        robot.health -= Dinosaur.attack_power
        print(f'{robot.name } now has {robot.health} remaining')