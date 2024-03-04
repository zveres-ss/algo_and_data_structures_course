import unittest
from src.ArrayZigzagTraversalLab import arr_zigzag_traverse


class Lab1Test(unittest.TestCase):
    def test_arr_zigzag_traverse_5x5(self):
        test_arr = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        test_n = 5
        test_m = 5
        needed_result = [25, 24, 20, 15, 19, 23, 22, 18, 14, 10, 5,
                         ]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_4x2(self):
        test_arr = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        test_n = 4
        test_m = 2
        needed_result = [1, 2, 3, 5, 4, 6, 7, 8]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_1x6(self):
        # тут все ок, просто масив списком виводиться, але тест все рівно матюкається
        test_arr = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        test_n = 6
        test_m = 1
        needed_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_1x1(self):
        test_arr = [
            [1]
        ]
        test_n = 1
        test_m = 1
        needed_result = [1]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")


if __name__ == '__main__':
    unittest.main()
