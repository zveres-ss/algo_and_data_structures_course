import unittest
from src.electrical_workers import max_wire_length

class TestMaxWireLength(unittest.TestCase):

    def test_example_1(self):
        expected_length = 5.65
        actual_length = max_wire_length(2, [3, 3, 3])

    def test_example_2(self):
        self.assertEqual(max_wire_length(100, [1, 1, 1, 1]), 300)

    def test_example_3(self):
        self.assertAlmostEqual(max_wire_length(4, [100, 2, 100, 2, 100]), 396.32, places=2)

    def test_example_4(self):
        expected_length = 2074.58
        actual_length = max_wire_length(4, [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72])


if __name__ == "__main__":
    unittest.main()
