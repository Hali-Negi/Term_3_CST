import abc

class Bird(abc.ABC):

    @abc.abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    def fly(self):
        print("Flying")

@Bird.register
class Robin:
    pass


p = Parrot()
p.fly()
r = Robin()
print(issubclass(Robin, Bird))
print(isinstance(r, Bird))
