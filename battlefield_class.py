from random import randint
from dinosaurs_class import Dinosaur
from robots_class import Robot

class Battlefield:

    def __init__(self) -> None:
        self.robot = Robot('Ratchet')
        self.dinosaur = Dinosaur('Bones',20)

    def display_welcome(self):
        print(f'welcome the wasteland where technology and primal carnage rage in an epic battle')

    def run_game(self):
        for random in range(10):
            first_turn = randint(0,10)
            if first_turn == (0,2,4,6,8,10):
                dinosaur_attacks = Dinosaur.Dinosaur_attack
            elif first_turn == (1,3,5,7,9):
                robot_attacks = Robot.robot_attack
        while Dinosaur.health >= 0 or Robot.health >= 0:
            if dinosaur_attacks:
                robot_attacks
            elif robot_attacks:
                dinosaur_attacks