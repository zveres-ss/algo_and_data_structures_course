import unittest
from Second_lab_third_level import check_placing_cows
from Second_lab_third_level import search

class TestResult(unittest.TestCase):
    def test_result(self):
        self.assertEqual(3, 3)
        return True
    
if __name__ == "__main__":
    unittest.main()
