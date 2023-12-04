class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    # викликаємо функцію для лівого та правого піддерева
    left_inverted = invert_binary_tree(tree.left)
    right_inverted = invert_binary_tree(tree.right)

    # вузол для дзеркального дерева
    inverted_tree = BinaryTree(tree.value)
    inverted_tree.left = right_inverted
    inverted_tree.right = left_inverted

    return inverted_tree

# обходим дерево

def in_order_traversal(node):
    if node is None:
        return
    # ліва гілка
    in_order_traversal(node.left)
    print(node.value, end=" ")
    # права гілка
    in_order_traversal(node.right)


# Значення в деревах ф виклик
if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    print("In-order traversal of the constructed tree is:")
    in_order_traversal(root) # обхід стокового

    inverted_root = invert_binary_tree(root)

    print("\nIn-order traversal of the inverted tree is:")
    in_order_traversal(inverted_root) # обіхд нового


import unittest

class TestBinaryTreeFunctions(unittest.TestCase):
    def test_invert_binary_tree(self):
        # Тест на порожньому дереві
        self.assertIsNone(invert_binary_tree(None))

    def test_in_order_traversal(self):
        # Тест на порожньому дереві
        self.assertIsNone(in_order_traversal(None))


if __name__ == '__main__':
    unittest.main()
