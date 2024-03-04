#   Рівень 3
#   Варіант 1
#   Для заданого бінарного дерева та конкретної вершини в цьому дереві
#   реалізуйте функцію пошуку наступного елемента під час серединного проходу
#   (in-order traversal). Наступник - це вузол, який має значення більше
#   за заданий вузол і знаходиться найближче до нього при серединному обході.
#
#   Нехай у вас задане бінарне дерево такого вигляду:
#
#       10
#      /  \
#     5    15
#    / \     \
#   3   7    20
#            /
#           12
#
#   Для вершини зі значенням 7, наступник - це вузол зі значенням 10.
#   Функція отримує на вхід корінь бінарного дерева та
#   вершину, для якої потрібно знайти наступника.


class BinaryTree:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    return node


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.left = BinaryTree(2, tree)
    tree.right = BinaryTree(3, tree)
    tree.left.left = BinaryTree(4, tree.left)
    tree.right.left = BinaryTree(5, tree.right)
    tree.left.right = BinaryTree(6, tree.left)
    tree.right.right = BinaryTree(7, tree.right)
