import unittest


def max_experience(levels, experience):
    dp = [[0] * (i + 1) for i in range(levels)]

    for j in range(levels):
        dp[levels - 1][j] = experience[levels - 1][j]

    for i in range(levels - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = experience[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]


class TestMaxExperience(unittest.TestCase):
    def test_three_levels(self):
        levels = 4
        experience = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1],
        ]
        self.assertEqual(max_experience(levels, experience), 12)

    def test_single_level(self):
        levels = 1
        experience = [[9999]]
        self.assertEqual(max_experience(levels, experience), 9999)

    def test_five_levels(self):
        levels = 5
        experience = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ]
        self.assertEqual(max_experience(levels, experience), 3)


if __name__ == "__main__":
    unittest.main()
