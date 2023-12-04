class UnionFind:
    def __init__(self, N):
        self.parent = {}
        self.rank = {}

        for vertex in N:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                return root2, root1
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                return root1, root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1
                return root2, root1

    def count_cross_tribe_pairs(self, pairs):
            boys = set()
            girls = set()

            for pair in pairs:
                x, y = pair
                if x % 2:
                    boys.add(x)
                else:
                    girls.add(x)
                if y % 2:
                    boys.add(y)
                else:
                    girls.add(y)

            counter = 0
            for girl in girls:
                for boy in boys:
                    root_girl = self.find(girl)
                    root_boy = self.find(boy)
                    if root_girl != root_boy:
                        counter += 1

            return counter

if __name__ == '__main__':

        N = [1, 2, 3, 4, 5, 6, 7, 8]
        pairs = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8)]

        unionFind = UnionFind(N)

        result_pairs = []
        for pair in pairs:
            x, y = pair
            result_pairs.append(unionFind.union(x, y))

        # Рахуємо кількість пар
        result = unionFind.count_cross_tribe_pairs(result_pairs)
        print("Кількість можливих пар хлопців і дівчаток:", result)