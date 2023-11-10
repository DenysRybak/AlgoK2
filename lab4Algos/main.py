from collections import deque # викорисовуємо чергу deque

class Node:
    def __init__(self, key):
        self.data = key
        self.children = []

def minDepth(root):
    if not root:
        return 0

    queue = deque() #черга створюється для обходу в ширину
    queue.append(root)
    depth = 1

    while queue:
        level_size = len(queue) # ількість вуздів на рівні

        for i in range(level_size): # перебор всіх вузлів
            node = queue.popleft()

            if not node.children:
                return depth

            for child in node.children: # всі дочірні вузли ноду(для обходу наступного)
                queue.append(child)

        depth += 1

edges = [] # дані з файлу

# Зчитуємо дані з файлу input.txt та будуємо граф
with open('input.txt', 'r') as file:
    lines = file.readlines() # читаємо і перебираємо інфу
    for line in lines:
        edge = line.strip().split(',')
        if len(edge) == 2: # перевірка на праивльнівсть
            edges.append([int(edge[0]), int(edge[1])])

node_dict = {} # словник для відстеження вузлів (графа з ключами)
root = None

for edge in edges: # перебираємо всі ребра
    parent_key, child_key = edge
    parent = node_dict.get(parent_key, None)
    child = node_dict.get(child_key, None)

    if not parent:
        parent = Node(parent_key) # створення новго парент вузла
        node_dict[parent_key] = parent
        if not root:
            root = parent

    if not child:
        child = Node(child_key)
        node_dict[child_key] = child

    parent.children.append(child)

# Обчислюємо мінімальну глибину в ширину
min_depth = minDepth(root)

# Записуємо результат в файл output.txt
with open('output.txt', 'w') as file:
    file.write(str(min_depth))
