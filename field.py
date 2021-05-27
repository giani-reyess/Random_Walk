

class Field:

    def __init__(self):
        # creating an empty dictionary where we gonna save the coordinates
        self.drunken_coordinates = {}  

    def add_drunken(self, drunken, coordinates):
        # adding drunkens using drunken parameter as keys of the dictionary, 
        # and coordinates parameter as values
        self.drunken_coordinates[drunken] = coordinates

    def move_drunken(self, drunken):
        # saving the tuple of values (returned by walk function) 
        # in the following variables: delta_x and delta_y 
        delta_x, delta_y = drunken.walk()
        # saving the lastest coordinate (inside the drunken_coordinates dictionary), 
        # in the variable actual_coordinates, using the key: drunken
        actual_coordinates = self.drunken_coordinates[drunken]
        # taking the lastest coordinate (inside the drunken_coordinates dictionary) 
        # with the drunken key, and save it as a new instance of class Coordinartes
        # by using the function move  
        new_coordinates = actual_coordinates.move(delta_x, delta_y)# = drunken.walk() 
        # save the new instance in the drunken_coordinates dictionary 
        self.drunken_coordinates[drunken] = new_coordinates

    def get_coordinates(self, drunken):
        return self.drunken_coordinates[drunken]