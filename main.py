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

# Классы героев
class Hero(ABC):
    def __init__(self, name, health, ability, weapon):
        self.name = name
        self.health = health
        self.ability = ability
        self.weapon = weapon

    @abstractmethod
    def set_ability(self):
        pass

    def attack(self, enemy):
        if self.health <= 0 or enemy.health <= 0:
            return

        multiplier = 1.4 if self.ability.lower() == "magical" and self.weapon.attack_type() == "magical" else 1.5 if self.ability.lower() == "physical" and self.weapon.attack_type() == "physical" else 1
        damage = random.randint(self.weapon.min_damage, self.weapon.max_damage) * multiplier

        print(f"{self.name} атакует {enemy.name}, нанося {damage:.1f} {self.weapon.attack_type()} урона!")
        time.sleep(1)  # Задержка перед следующим сообщением
        enemy.health -= damage
        if enemy.health > 0:
            print(f"У {enemy.name} осталось {enemy.health:.1f} кол-ва здоровья")
        else:
            enemy.health = 0
            print(f"{enemy.name} погиб!")

    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} погиб!")
            return True
        return False

class Wizard(Hero):
    def set_ability(self):
        print(f"{self.name} имеет аспект {self.ability}. Его урон от магии увеличен на 40%!")
        time.sleep(1)  # Задержка перед следующим сообщением

class Warrior(Hero):
    def set_ability(self):
        print(f"{self.name} имеет аспект {self.ability}. Его физический урон увеличен на 50%!")
        time.sleep(1)  # Задержка перед следующим сообщением