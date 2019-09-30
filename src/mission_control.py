from .rover import Rover
from .compass import Compass
from .plateau import Plateau

class MissionControl:
    def __init__(self):
        self.plateau = Plateau()
        self.rover = Rover()

    def plateau_area(self, x = 0, y = 0):
        self.plateau.position_x = int(x)
        self.plateau.position_y = int(y)

    def rover_position(self, x = 0, y = 0):
        self.rover.position_x = int(x)
        self.rover.position_y = int(y)

    def rover_direction(self, direction = 0):
        self.rover.direction = Compass.directions.index(direction)

    def command(self, command_list = ''):
        for command in command_list:
            if command is 'R':
                self.rover.turn_right()

            if command is 'L':
                self.rover.turn_left()

            if command is 'M':
                try:
                    self.plateau.detect_boundaries(self.rover)
                    self.rover.move()
                except Exception as e:
                    print(str(e))
                    break

        return str(self.rover.position_x) + " " + str(self.rover.position_y)  + " " + Compass.directions[self.rover.direction]
