class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode) -> int:
    def dfs(node, depth):
        if not node:
            return 0
        return depth + dfs(node.left, depth + 1) + dfs(node.right, depth + 1)

    return dfs(root, 0)
