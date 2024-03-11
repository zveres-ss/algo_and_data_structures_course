import unittest
from First_lab_second_level import sort
from First_lab_second_level import k_founder

class TestCode(unittest.TestCase):
    def test_sort(self):
        self.assertEqual("Знайдений 3-й за величиною елемент: 22", "Знайдений 3-й за величиною елемент: 22")
        self.assertEqual("Позиція 3-го найбільшого елемента: 2", "Позиція 3-го найбільшого елемента: 2")

if __name__ == "__main__":
    unittest.main()