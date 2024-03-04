from src.BinaryHamstersSearchLab import how_many_hamsters
import unittest


class Lab2Test(unittest.TestCase):
    # task tests
    def test_example1(self):
        S = 7
        C = 3
        hamsters = [
            [1, 2],
            [2, 2],
            [3, 1]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 2)

    def test_example2(self):
        S = 19
        C = 4
        hamsters = [
            [5, 0],
            [2, 2],
            [1, 4],
            [5, 1]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 3)

    def test_example3(self):
        S = 2
        C = 2
        hamsters = [
            [1, 50000],
            [1, 60000]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 1)

    # gpt tests
    def test_basic_case(self):
        hamsters = [
            [10, 5],
            [8, 4],
            [7, 3]
        ]
        C = 3
        S = 30
        self.assertEqual(how_many_hamsters(hamsters, C, S), 2)

    def test_no_hamsters_needed(self):
        hamsters = [
            [10, 5],
            [8, 4],
            [7, 3]
        ]
        C = 3
        S = 5
        self.assertEqual(how_many_hamsters(hamsters, C, S), 1)

    def test_empty_hamsters_list(self):
        hamsters = []
        C = 5
        S = 30
        self.assertEqual(how_many_hamsters(hamsters, C, S), 0)

    def test_zero_S(self):
        hamsters = [
            [10, 5],
                    [8, 4],
                    [7, 3]
                    ]
        C = 3
        S = 0
        self.assertEqual(how_many_hamsters(hamsters, C, S), 0)

    # student tests
    def v_test(self):
        hamsters = [
            [17, 3],
            [8, 4],
            [7, 3]
        ]
        C = 3
        S = 30
        self.assertEqual(how_many_hamsters(hamsters, C, S), 2)

    def my_test(self):
        hamsters = [
            [4, 2],
            [2, 3],
            [1, 4],
            [6, 2],
            [1, 5]
        ]
        C = 5
        S = 29
        self.assertEqual(how_many_hamsters(hamsters, C, S), 2)

    def test_all_greedy_hamsters(self):
        S = 24
        C = 4
        hamsters = [
            [5, 2],
            [5, 3],
            [2, 1],
            [5, 5]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 3)


if __name__ == '__main__':
    unittest.main()
