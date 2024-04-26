import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from k_largest_element import k_founder, sort, array, error

class TestFunctions(unittest.TestCase):
    def test_sort(self):
        temp = [2, 7, 9, 15, 18, 22, 36, 42]
        sort(0, array, len(array) - 1)
        self.assertEqual(array, temp)

    def test_k_founder(self):
        self.assertEqual(k_founder(array, 1), (42, 6))
        self.assertEqual(k_founder(array, 3), (22, 2))
        self.assertEqual(k_founder(array, 8), (2, 5))

if __name__ == '__main__':
    unittest.main()
