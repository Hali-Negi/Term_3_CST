"""
In python, a single py file is called a module. There should always be a
short docstring comment at the top explaining the purpose of the module.
"""

print("This code will execute whenever this module is run or imported.")
print(f"The __name__ builtin value of module_example.py is {__name__}")

def some_function():
    """
    This function will also be "evaluated" when this module is
    run/imported. The interpreter will define the function when it
    encounters this definition.
    """
    print("I am some_function")

if __name__ == '__main__':
    print("This code will only execute when this module is the entry point "
          "of the program.")