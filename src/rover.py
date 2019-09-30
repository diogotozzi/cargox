from .compass import Compass

class Rover:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.direction = 0

    def turn_left(self):
        self.direction -= 1

        if self.direction < 0:
            self.direction = 3

    def turn_right(self):
        self.direction += 1

        if self.direction > 3:
            self.direction = 0

    def move(self):
        if self.direction is Compass.E:
            self.position_x += 1

        if self.direction is Compass.W:
            self.position_x -= 1

        if self.direction is Compass.N:
            self.position_y += 1

        if self.direction is Compass.S:
            self.position_y -= 1
