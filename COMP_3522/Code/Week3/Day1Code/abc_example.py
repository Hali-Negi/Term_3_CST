import abc

# must inherit from ABC to enforce subclasses fully implement methods


class Bird(abc.ABC):

    # tags method as abstract. Subclasses MUST implement
    @abc.abstractmethod
    def fly(self):
        pass

    @abc.abstractmethod
    def lay_egg(self):
        pass


class Parrot(Bird):
    # these methods fully implement abstract methods from parent class
    def fly(self):
        print("Flying")

    # try not including this method, see what happens when running code
    def lay_egg(self):
        print("laying egg")


p = Parrot()
p.fly()
p.lay_egg()
