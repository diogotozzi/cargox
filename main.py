from src.rover import Rover
from src.compass import Compass
from src.plateau import Plateau

import fileinput
import json

def main():
    rover = Rover()
    plateau = Plateau()

    for line in fileinput.input():
        # First line - Plateau size
        if fileinput.lineno() is 1:
            plateau.position_x = int(line[0])
            plateau.position_y = int(line[2])

        if not fileinput.isfirstline():
            # Rover line
            if fileinput.lineno() % 2 is 0:
                rover.position_x = int(line[0])
                rover.position_y = int(line[2])

                rover.direction = Compass.directions.index(line[4])

            # Movements line
            if fileinput.lineno() % 2 is not 0:
                for movement in line:
                    if movement is 'R':
                        rover.turn_right()

                    if movement is 'L':
                        rover.turn_left()

                    if movement is 'M':
                        try:
                            plateau.detect_boundaries(rover)
                            rover.move()
                        except Exception as e:
                            print(str(e))
                            break

                print(str(rover.position_x) + " " + str(rover.position_y)  + " " + Compass.directions[rover.direction])

main()
