from drunken import TraditionalDrunken
from field import Field
from coordinates import Coordinates


def hike(field, drunken, steps):
    start = field.get_coordinates(drunken)
    for _ in range (steps):
        field.move_drunken(drunken)   
    return start.distance(field.get_coordinates(drunken))



def simulate_hike(steps, iterations, kind_of_drunken):
    drunken = kind_of_drunken(name='Giani')
    orirgin = Coordinates(0,0)
    distance = []

    for _ in range(iterations):
        field = Field()
        field.add_drunken(drunken, orirgin)
        hike_simulation = hike(field, drunken, steps)
        distance.append(round(hike_simulation, 1))

    return distance    



def main(range_distance, iterations , kind_of_drunken):	
	for steps in hike_distance:
            distances = simulate_hike(steps, iterations, kind_of_drunken)
            mid_distance = round(sum(distances) / len(distances), 4)
            max_distance = max(distances)
            minimal_distance = min(distances)

            print(f'{kind_of_drunken.__name__} random walk of {steps}')
            print(f'Media = {mid_distance}')
            print(f'Max = {max_distance}')
            print(f'Min = {minimal_distance}')


if __name__ == '__main__':

	hike_distance = [10,100,1000,10000]
	iterations = 100

	main(hike_distance, iterations,TraditionalDrunken)