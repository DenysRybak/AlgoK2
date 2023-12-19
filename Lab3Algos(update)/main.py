class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    # зберігаємо вузли в стеку
    stack = [tree]

    # старт ітерації поки є стек
    while stack:
        node = stack.pop()

        # Міняємо ліве і праве піддерево
        node.left, node.right = node.right, node.left

        # перевірка вузла у ноді
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return tree

# обходим дерево і друкуємо значення в ін - ордер
def in_order_traversal(node):
    if node is None:
        return

    stack = []
    current = node

    # ідерація доки стек не буде пустим
    while stack or current:
        if current: # існує вузол?
            stack.append(current)
            current = current.left
        else: # вилучаємо вузол із стеку
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right

if __name__ == "__main__":
    root = BinaryTree(1)

    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    print("In-order traversal of the constructed tree is:")
    in_order_traversal(root)

    inverted_root = invert_binary_tree(root)

    print("\nIn-order traversal of the inverted tree is:")
    in_order_traversal(inverted_root)

import unittest

class TestBinaryTreeFunctions(unittest.TestCase):
    # Тест на те чи правильно розвертається дерево
    def test_invert_binary_tree(self):
        # Тест на порожнього дерева
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
