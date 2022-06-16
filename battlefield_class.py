from logging import root
from random import randint, random
from dinosaurs_class import Dinosaur
from robots_class import Robot

class Battlefield:

    def __init__(self) -> None:
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def display_welcome(self):
        print('\nYou and your fellow Replicant guards are standing hold at the entrance of your stronghold')
        print('Suddenly a group of Dinosaurs charge you!')
        print('ready your weapons and prepare to be your lands last defence!')
        print('')

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.winner_phase()

    def battle(self):         
        while self.dinosaur.health > 0 and self.robot.health > 0:
            first_turn = randint(0,10)
            if first_turn == (0 or 2 or 4 or 6 or 8 or 10):
                self.dinosaur.attack(self.robot)
                if self.robot.health > 0:
                    self.robot.attack(self.dinosaur)
            elif first_turn == (1 or 3 or 5 or 7 or 9):
                self.robot.attack(self.dinosaur)   
                if self.dinosaur.health > 0:
                    self.dinosaur.attack(self.robot)

    def winner_phase(self):
        if self.dinosaur.health >0:
            print("")
            print('The dinosaurs broke past your defence and into the prison. \nThey stole the dinosaurs you had captive for fuel.\nWe must take our fuel back from the carbon life on this planet')
            print('')
        elif self.robot.health >0:
            print('thank you for your sacrafice carbon lifeform your kind will continue to fuel our distruction of the planets')
            print('')