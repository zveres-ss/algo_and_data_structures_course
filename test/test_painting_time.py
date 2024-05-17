import unittest

def time_to_paint(K, T, L):
    L.sort(reverse=True)
    painters_time = [0] * K
    for length in L:
        min_time_index = painters_time.index(min(painters_time))
        painters_time[min_time_index] += length * T
    return max(painters_time)

class TestTimeToPaint(unittest.TestCase):
    def test_example(self):
        K = 10
        T = 5
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(time_to_paint(K, T, L), 50)

    def test_1_painter(self):
        K = 1
        T = 5
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
        self.assertEqual(time_to_paint(K, T, L), sum(L) * T)

    def test_painters_more_than_boards(self):
        K = 15
        T = 5
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

        self.assertEqual(time_to_paint(K, T, L), max(L) * T)

    def test_empty(self):
        K = 5
        T = 5
        L = []
        self.assertEqual(time_to_paint(K, T, L), 0)

if __name__ == '__main__':
    unittest.main()