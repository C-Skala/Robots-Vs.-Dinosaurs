from robots import Robot

class Dinosaur:

    def __init__(self) -> None:
        self.name = 'bones'
        self.attack_power = 20
        self.health = 100

    def Dinosaur_attack(self):
        print(f'{Dinosaur.name} attaks {Robot.name} with its powerfull jaws for {Dinosaur.attack_power}')
        Robot.health -= Dinosaur.attack_power
        print(f'{Robot.name} now has {Robot.health} remaining')