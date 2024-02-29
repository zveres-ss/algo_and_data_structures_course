import unittest

def is_monotonic(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr or arr[::-1] == sorted_arr

class TestIsMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))

    def test_nonmonotonic(self):
        self.assertFalse(is_monotonic([1, 2, 3, 5, 4]))
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))
        self.assertFalse(is_monotonic([1, 2, 3, 2, 5]))
        self.assertTrue(is_monotonic([1, 2, 3, 3, 3]))
        self.assertTrue(is_monotonic([1, 1, 1, 1, 1]))

    def test_empty(self):
        self.assertTrue(is_monotonic([]))

if __name__ == '__main__':
    unittest.main()
