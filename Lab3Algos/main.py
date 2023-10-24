class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# перевірка вузла на відсутність дочірніх вузлів (листок)
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

# обчислення суму лівих гілок
def branchSums(root):

    res = 0

    # перевірка корення на пустоту
    if root is not None:

        # перевірка лівого на те чи є листком і вводить корені ліві
        if isLeaf(root.left):
            res += root.left.value
        else:
            # підрахування
            res += branchSums(root.left)


        # підрахунок правого
        res += branchSums(root.right)
    return res


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

print("Sum of left leaves is", branchSums(root))
