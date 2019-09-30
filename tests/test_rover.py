from src.rover import Rover

import unittest

class TestRover(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic_move(self):
        rover = Rover()
        rover.move()

        self.assertEqual(rover.position_x, 1)
        self.assertEqual(rover.position_y, 0)

    def test_advanced_move(self):
        rover = Rover()

        rover.position_x = 5
        rover.position_y = 5
        rover.direction = 3

        rover.move()

        self.assertEqual(rover.position_x, 5)
        self.assertEqual(rover.position_y, 6)
