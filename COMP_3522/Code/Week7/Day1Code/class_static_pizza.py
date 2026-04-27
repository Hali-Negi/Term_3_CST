"""
This module demonstrates different uses of instance, class, and static methods
"""

#https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Class%20methods%20don't%20need,belong%20to%20the%20class's%20namespace.

import math

class Pizza:

    PERSONAL_SIZE = 7
    FAMILY_SIZE = 14
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius}, '
                f'{self.ingredients})')

    def area(self):
        return self.circle_area(self.radius)

    # the following two class methods are factory functions. Simple helper
    # methods to hide the implementation of creating a very specific type of pizza
    @classmethod
    def margherita(cls):
        return cls(cls.FAMILY_SIZE, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(cls.FAMILY_SIZE, ['mozzarella', 'tomatoes', 'ham'])

    # static method not using the instance or class of Pizza, but
    # contains helpful code, tangentially related to pizzas
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(Pizza.PERSONAL_SIZE, ['pineapple', 'mozzarella'])
print(p)
print(p.area())

# Class and static methods belong to the class
# Preferred approach to calling class or static methods
# Use the class name (Pizza) to call class or static methods
print(Pizza.margherita())
print(Pizza.prosciutto())
print(Pizza.circle_area(Pizza.PERSONAL_SIZE))
#print(Pizza.area()) #Can't can instance method with Class. TypeError: Pizza.area() missing 1 required positional argument: 'self'

# # Non preferred approach: instance variable can be used to call class or static methods
# print(p.margherita())
# print(p.prosciutto())
# print(p.circle_area(Pizza.PERSONAL_SIZE))

"""
Quote from site:
"Using static methods and class methods are ways to communicate developer 
intent while enforcing that intent"
"""
