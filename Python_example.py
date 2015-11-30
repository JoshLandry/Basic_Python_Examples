from classes import *
import unittest

instance_of_Triangle = Triangle(60,60,60)

class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(instance_of_Triangle.angle1 == 60)

    def test_assert_false(self):
        self.assertFalse(instance_of_Triangle.angle2 == 80)

    def test_angle_sum(self):
        self.assertTrue(instance_of_Triangle.sum_angles() == 180)

if __name__ == '__main__':
    unittest.main()