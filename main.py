from src.mission_control import MissionControl

import fileinput
import json

def main():
    mission_control = MissionControl()

    for line in fileinput.input():
        # First line - Plateau size
        if fileinput.lineno() is 1:
            mission_control.plateau_area(line[0], line[2])

        if not fileinput.isfirstline():
            # Rover line
            if fileinput.lineno() % 2 is 0:
                mission_control.rover_position(line[0], line[2])
                mission_control.rover_direction(line[4])

            # Movements line
            if fileinput.lineno() % 2 is not 0:
                result = mission_control.command(line)
                print(result)
main()
