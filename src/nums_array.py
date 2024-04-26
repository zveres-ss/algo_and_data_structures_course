import unittest

nums = [-4, -2, 0, 1, 3]
square = [i**2 for i in nums]


def bubble(nums):
    length = len(nums) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, length):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


class TestSort(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(bubble([0, 1, 4, 9, 16]), [0, 1, 4, 9, 16])
        self.assertEqual(bubble([1, 4, 9, 16, 25]), [1, 4, 9, 16, 25])


if __name__ == "__main__":
    unittest.main()
