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
    # Тест на те чи правильно розвертається дерево
    def test_invert_binary_tree(self):
        # Тест на порожньому дереві
        self.assertIsNone(invert_binary_tree(None))

        # Тест на одному вузлі
        tree = BinaryTree(1)
        inverted_tree = invert_binary_tree(tree)
        self.assertEqual(inverted_tree.value, 1)
        self.assertIsNone(inverted_tree.left)
        self.assertIsNone(inverted_tree.right)

        # Тест на дереві з багатьма вузлами
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_root = invert_binary_tree(root)

        # Перевірка дзеркального дерева
        self.assertEqual(inverted_root.value, 1)
        self.assertEqual(inverted_root.left.value, 3)
        self.assertEqual(inverted_root.right.value, 2)
        self.assertEqual(inverted_root.left.left.value, 7)
        self.assertEqual(inverted_root.left.right.value, 6)
        self.assertEqual(inverted_root.right.left.value, 5)
        self.assertEqual(inverted_root.right.right.value, 4)

    def test_in_order_traversal(self):
        # Тест на порожньому дереві
        self.assertIsNone(in_order_traversal(None))


if __name__ == '__main__':
    unittest.main()
