import module_example
# math is one of the built in modules that comes with python!
import math

# This is the preferred way of importing a module. Only import what you
# need.
# from module_example import some_function

# subsequent imports wont work if the whole module has already been imported
# import module_example

print("The import statement will run all the code in the module that is "
      "being imported. A module cannot be imported more than once and any "
      "subsequent calls to import will be ignored like the one below.")
print(f"The __name__ builtin value of import_example.py is {__name__}")

# This function call will execute only with the first import statement.
module_example.some_function()


# This function call will execute only with the second import statement.
# some_function()

def hypotenuse(a, b):
    """
    Given the length of two sides fo a right angled triangle,
    this calculates function calculates the length of the hypotenuse.
    :param a: an int or a float
    :param b: an int or a float
    :return: an int or a float, hypotenuse
    """
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    # An example of formatting floats into strings
    print(f"The hypotenuse is {hypotenuse(5, 3):.2f}.")
