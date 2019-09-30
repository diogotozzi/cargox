from .compass import Compass
from .rover import Rover

class Plateau:
    def __init__(self, x = 0, y = 0):
        self.position_x = x
        self.position_y = y

    def detect_boundaries(self, rover = Rover()):
        if self.predict_move(rover):
            raise Exception("! COLLISION ALERT - OUT OF PLATEAU'S BOUNDARIES !")

    def predict_move(self, rover = Rover()):
        collision = False

        if rover.direction is Compass.E:
            if rover.position_x == self.position_x:
                collision = True

        if rover.direction is Compass.W:
            if rover.position_x == 0:
                collision = True

        if rover.direction is Compass.N:
            if rover.position_y == self.position_y:
                collision = True

        if rover.direction is Compass.S:
            if rover.position_y == 0:
                collision = True

        return collision
