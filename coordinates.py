
class Coordinates:

    def __init__(self, x, y):
        # self.x and self.y are our initial coordinates  
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        # return the new coordinates with its new position
        return Coordinates(self.x + delta_x, self.y + delta_y) 
        # by create a new instance each time we run a new simulation

    def distance(self, new_coordinate):
        # calculate the distance between the initial coordinate and the new one
        delta_x = self.x - new_coordinate.x
        delta_y = self.y - new_coordinate.y
        # by subtrackting initial coordinates with the new ones 
        # to get the legs of the triangle   
        return (delta_x**2 + delta_y**2)**0.5
        # and then use the Pythagoras Theorem 
