import unittest
from src.boyer_moore import boyer_moore_search


class TestBoyerMooreSearch(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(boyer_moore_search("abracadabra", "abra"), [0, 7])
        self.assertEqual(boyer_moore_search("aaaaaaa", "aa"), [0, 1, 2, 3, 4, 5])
        self.assertEqual(boyer_moore_search("hello world", "world"), [6])
        self.assertEqual(boyer_moore_search("hello world", "o"), [4, 7])
        self.assertEqual(boyer_moore_search("hello", "ll"), [2])

    def test_no_occurrences(self):
        self.assertEqual(boyer_moore_search("abracadabra", "xyz"), [])
        self.assertEqual(boyer_moore_search("hello world", "abc"), [])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abracadabra", ""), [])
        self.assertEqual(boyer_moore_search("", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abra"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("abc", "abcd"), [])

    def test_same_needle_and_haystack(self):
        self.assertEqual(boyer_moore_search("abc", "abc"), [0])


if __name__ == "__main__":
    unittest.main()
