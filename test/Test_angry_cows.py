import unittest
import os
import sys
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
from angry_cows import check_placing_cows, search, check_numbers_of_cows, check_sections, free_sections, sort

class TestFunctions(unittest.TestCase):
    def test_check_sections(self):
        self.assertEqual(check_sections(10), None)
        self.assertEqual(check_sections(100000), None)

    def test_check_numbers_of_cows(self):
        self.assertEqual(check_numbers_of_cows(3, 5), None)
        self.assertEqual(check_numbers_of_cows(5, 3), None)

    def test_sort(self):
        temp = [1, 2, 4, 8, 9]
        sort(0, free_sections, len(free_sections) - 1)
        self.assertEqual(free_sections, temp)

    def test_check_placing_cows(self):
        self.assertTrue(check_placing_cows(free_sections, 3, 3))
        self.assertFalse(check_placing_cows(free_sections, 10, 3))

    def test_search(self):
        self.assertEqual(search(free_sections, 3), 3)
        self.assertEqual(search(free_sections, 4), 7)

if __name__ == '__main__':
    unittest.main()
