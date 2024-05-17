import unittest
from src.sum_of_depths import TreeNode, sum_of_depths


class TestSumOfDepths(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(sum_of_depths(root), 1 + 1)

    def test_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 0 + 1 + 1 + 2 + 2)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(8)
        root.right = TreeNode(3)
        root.right.right = TreeNode(7)
        self.assertEqual(sum_of_depths(root), 0 + 1 + 1 + 2 + 3 + 2)

    def test_empty_tree(self):
        root = None
        self.assertEqual(sum_of_depths(root), 0)


if __name__ == "__main__":
    unittest.main()
