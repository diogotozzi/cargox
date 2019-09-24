from rover import Rover

import fileinput
import json

def main():
    rover = Rover()

    for line in fileinput.input():

        # if fileinput.lineno() is 1:
        #     map_x = line[0]
        #     map_y = line[2]

        if not fileinput.isfirstline():
            if fileinput.lineno() % 2 is 0:
                rover.position_x = line[0]
                rover.position_y = line[2]
                rover.direction = rover.directions.index(line[4])

            if fileinput.lineno() % 2 is not 0:
                # print(rover.direction)
                # rover.directions[::-1]

                for movement in line:
                    if movement is 'R':
                        a = iter(rover.directions)
                        print(next(a))

                    if movement is 'L':
                        a = rover.directions
                        a.reverse()
                        a = iter(a)
                        print(next(a))

main()
