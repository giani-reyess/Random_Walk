import random

# This class define the name of the drunken
class Drunken:
    def __init__(self, name):
        self.name = name

# And this one define the behavior of the drunken 
# with the inherited name by the class Drunken 
class TraditionalDrunken(Drunken):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

