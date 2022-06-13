from weapons import Weapon
from dinosaurs import Dinosaur  

class Robot:

    def __init__(self) -> None:
        self.name = 'ratchet'
        self.health = 100
        self.active_weapon = Weapon()

