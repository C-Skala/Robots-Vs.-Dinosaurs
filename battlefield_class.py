from random import randint, random
from dinosaurs_class import Dinosaur
from robots_class import Robot

class Battlefield:

    def __init__(self) -> None:
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def display_welcome(self):
        print(f'welcome the wasteland where technology and primal carnage rage in an epic battle')

    def run_game(self):
        self.display_welcome()
        self.battle()


        
    def battle(self):         
        while self.dinosaur.health >= 0 or self.robot.health >= 0:
            first_turn = (random,randint(0, 10))
            if first_turn == (0,2,4,6,8,10):
                self.dinosaur.attack() 
                self.robot.attack()
            elif first_turn == (1,3,5,7,9):
                self.robot.attack()   
                self.dinosaur.attack()





    