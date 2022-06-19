

from random import randint


class Dinosaur:

    def __init__(self) -> None:
        self.name = "Rex"
        self.attack_power = randint(20,25)
        self.health = randint(90,110)

    def attack(self, robot):
        print(f'{self.name} attaks {robot.name} with its powerfull jaws for {self.attack_power}')
        robot.health -= self.attack_power
        print(f'{robot.name } now has {robot.health} remaining')
        print('')