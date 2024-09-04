from abc import ABC, abstractmethod
import random
import time

# Классы оружия
class Weapon(ABC):
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage

    def __str__(self):
        return self.name

    @abstractmethod
    def attack_type(self):
        pass

class PhysicalWeapon(Weapon):
    def attack_type(self):
        return "physical"

class MagicalWeapon(Weapon):
    def attack_type(self):
        return "magical"