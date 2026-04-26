# Mixin class
class LoggingMixin:
    def log(self, message):
        print(f"Logging message: {message}")


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


# Combining the Mixin and the base class
class Dog(Animal, LoggingMixin):
    def make_sound(self):
        self.log(f"{self.name} says Woof!")


class Cat(Animal, LoggingMixin):
    def make_sound(self):
        self.log(f"{self.name} says Meow!")


# Usage
dog = Dog("Buddy")
dog.make_sound()  # Logs: Buddy says Woof!

cat = Cat("Whiskers")
cat.make_sound()  # Logs: Whiskers says Meow!
