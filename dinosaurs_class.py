

class Dinosaur:

    def __init__(self) -> None:
        self.name = 'bones'
        self.attack_power = 20
        self.health = 100

    def attack(self, robot):
        print(f'{self.name} attaks {robot.name} with its powerfull jaws for {self.attack_power}')
        robot.health -= self.attack_power
        print(f'{robot.name } now has {robot.health} remaining')