class AClass:
    def __init__(self, message):
        self.message = message

    #override __call__ method to enable calling AClass instance as if it's a function
    def __call__(self, message2):
        print(f"Object's message: {self.message}")
        print(f"Message passed in parameter: {message2}")

    #regular method
    def foo(self, message2):
        print(f"Object's message: {self.message}")
        print(f"Message passed in parameter: {message2}")


def main():
    callable_object = AClass("You just used an object like a function!")

    # callable_object.foo("Callable objects can also take in any parameters") #regular call to method
    callable_object("Callable objects can also take in any parameters") #call object as if it's a function
    callable_object.__call__("Callable objects can also take in any parameters") #call object as if it's a function


if __name__ == '__main__':
    main()