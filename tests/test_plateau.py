from src.plateau import Plateau
from src.rover import Rover

import unittest

class TestRover(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau()

        self.plateau.position_x = 5
        self.plateau.position_y = 5

    def tearDown(self):
        pass

    def test_not_detect_boundaries_move(self):
        rover = Rover()
        rover.move()

        self.assertEqual(rover.position_x, 1)
        self.assertEqual(rover.position_y, 0)

        self.assertEqual(False, self.plateau.detect_boundaries(rover))


    def test_detect_bondaries_move(self):
        rover = Rover()

        rover.position_x = 5
        rover.position_y = 5
        rover.direction = 3

        rover.move()

        self.assertEqual(rover.position_x, 5)
        self.assertEqual(rover.position_y, 6)

        self.assertRaises(Exception, lambda: self.plateau.detect_boundaries(rover))
