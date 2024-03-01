import unittest
from Laba_1.2.py import sort
from Laba_1.2.py import k_founder

class TestCode(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(
            "Знайдений 3-й за величиною елемент: 22",
            "Знайдений 3-й за величиною елемент: 22",
        )
        self.assertEqual(
            "Позиція 3-го найбільшого елемента: 6",
            "Позиція 3-го найбільшого елемента: 6",
        )

if __name__ == "__main__":
    unittest.main()