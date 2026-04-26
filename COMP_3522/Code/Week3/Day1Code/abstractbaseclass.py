"""
This module represents how an abstract base class can be used to
enforce objects to implement a common interface.
"""
import abc
import random


class Character(abc.ABC):
    """
    An Abstract Base Class that provides a simple interface that all
    characters need to implement. Any class that inherits from this
    class MUST implement all the @abstractmethods and
    @abstractclassmethods.
    """

    max_health = 200

    def __init__(self, name="Unnamed", health=10):
        self.name = name
        self._health = health

    def set_health(self, health):
        """
        Sets the health. This demonstrates that all methods in ABC's
        need not be @abstractmethods.
        :param health:
        """
        if health <= Character.max_health:
            self._health = health

    def attack(self, enemy, damage):
        enemy.take_damage(damage)

    @abc.abstractmethod
    def take_damage(self, damage):
        """
        Simulates the given character receiving damage. An abstract base
        class does not necessarily need to have empty methods, they may
        have common code that the child classes may want to re-use. The
        same as simple inheritance! We can now re-use code and force
        the child class to override it. This is something Java can't do.
        :param damage: a float
        """
        self._health -= damage

    @abc.abstractmethod
    def speak(self):
        """ Simulates the characters speech. """
        pass

    @staticmethod
    @abc.abstractmethod
    def a_static_method():
        print("random ")


class Player(Character):
    def __init__(self, name="Unnamed", health=10, lives=3):
        """
        Initializes a player object with a name, health and number of
        lives
        :param name: string
        :param health: a positive int
        :param lives: a positive int
        """
        self.set_lives(lives)
        super().__init__(name, health)

    def set_lives(self, lives):
        """
        Updates the lives of the player
        :param lives: a positive int
        """
        if lives >= 0:
            self._lives = lives

    def take_damage(self, damage):
        """
        Overrides the abstract method declared in the Character class.
        Notice how the child class doesn't add the @abstractmethod
        decorator
        :param damage: a float
        :return: current health
        """
        super().take_damage(damage)
        if self._health <= 0:
            self._health = self.original_health
            self._lives -= 1
            if self._lives <= 0:
                print(f"{self.name} has died. Game Over!")

    def speak(self):
        print(f"Greetings! I am {self.name}")

    def __str__(self):
        return f"Player {self.name}: \nHealth: {self._health} " \
            f"Lives: {self._lives}"

    @staticmethod
    def a_static_method():
        print("Player ")


class MutantRat(Character):

    def __init__(self, name="Unnamed", health=10, dodge_chance=0.1,
                 attack_power=5):
        self._dodge_chance = dodge_chance
        self._attack_power = attack_power
        super().__init__(name, health)

    def take_damage(self, damage):
        dodge = random.random()
        if dodge > self._dodge_chance:
            super().take_damage(damage)
            if self._health <= 0:
                print(f"{self.name} the Squeaker is dead.")
        else:
            print(f"{self._name} the Squeaker dodged the attack!")

    def speak(self):
        print(f"I am {self.name} the Squeaker!")

    def deal_damage(self):
        """
        Simulates attacking
        :return: a float, the potential damage dealt
        """
        return self._attack_power

    def __str__(self):
        return f"Mutant Rat {self.name}: \nHealth: {self._health} " \
            f"Dodge %: {self._dodge_chance} Attack Power: " \
            f"{self._attack_power}"

    @staticmethod
    def a_static_method():
        print("Mutant rat ")


def deal_damage_to_multiple_characters(character_list):
    """
    Simulates damage dealt to all characters specified. The Character
    Abstract Base Class now guarantees that any character would work
    with this method.
    :param character_list: a list(Characters)
    """
    for character in character_list:
        character.take_damage(5)
        print(character)


def main():
    """
    Maintains a list of characters and demonstrates polymorphism via
    Abstract Base Classes
    """
    player = Player("Zorak The Destroyer", 50, 2)
    print(player)
    print(f"Player {player.name} is an instance of Player: "
          f"{isinstance(player, Player)}")
    print(f"Player {player.name} is an instance of Character: "
          f"{isinstance(player, Character)}")
    print(f"Player {player.name} is an instance of MutantRat: "
          f"{isinstance(player, MutantRat)}", end="\n\n")

    scabbers = MutantRat("Scabbers", 70)
    print(scabbers)
    print(f"Mutant Rat {scabbers.name} is an instance of MutantRat: "
          f"{isinstance(scabbers, MutantRat)}")
    print(f"Mutant Rat {scabbers.name} is an instance of Character: "
          f"{isinstance(scabbers, Character)}")
    print(f"Mutant Rat {scabbers.name} is an instance of Player: "
          f"{isinstance(scabbers, Player)}")

    character_list = [player, scabbers]  # a list of characters
    deal_damage_to_multiple_characters(character_list)

    print("\n")
    print("Battle Simulation:")
    print("------------------")
    damage = scabbers.deal_damage()
    scabbers.attack(player, damage)
    print(f"{scabbers.name} attacks! Player {player.name} takes {damage}"
          f" damage!")
    print(player)

    print("\n")
    print("Class Variables")
    print("---------------")
    print("Setting Player 'max_health' class variable to 300")
    Player.max_health = 300
    print(f"Player Max Health: {Player.max_health}")
    print(f"Mutant Rat Max Health: {MutantRat.max_health}")
    print(f"Character Max Health: {Character.max_health}")

    Player.a_static_method()
    MutantRat.a_static_method()
    Character.a_static_method()

    print("NOTE: Each class maintains its own seperate instance of class"
          " variables. Different classes do not share their parents "
          "class variable instance")

    print(f"Is Scabbers' class a MutantRat? {scabbers.__class__ is MutantRat}")


if __name__ == '__main__':
    main()
