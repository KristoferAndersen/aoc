import math

class QU:
    def __init__(self, n) -> None:
        self.ids = list(range(n))
        self._count = n
        self.sizes = [1]*n

    def find(self, a) -> int:
        # root refers to itself
        if self.ids[a] != a:
            a = self.find(self.ids[a])

        return a

    def union(self, a, b) -> None:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        self.ids[root_a] = root_b
        self.sizes[root_b] += self.sizes[root_a]
        self._count -= 1

    def __str__(self) -> str:
        return f'{self.ids}'

    @property
    def count(self) -> int:
        return self._count

def to_p(s):
    return tuple(int(n) for n in s.split(','))

def build_distances(points):
    distances = []
    for i, a in enumerate(points[:-1]):
        for b in points[i+1:]:
            dist = eucl_dist(a, b)
            distances.append([dist, a, b])

    return distances

def solve_a(points):
    distances = build_distances(points)
    inverse_index = {p: i for i, p in enumerate(points)}

    qu = QU(len(points))
    distances.sort(key=lambda d: d[0])

    for d in distances[:1000]:
        ai = inverse_index[d[1]]
        bi = inverse_index[d[2]]
        qu.union(ai, bi)


    root_sizes = []
    for i, id in enumerate(qu.ids):
        if i == id:
            root_sizes.append(qu.sizes[i])

    return math.prod(n for n in list(reversed(sorted(root_sizes)))[:3])

def solve_b(points):
    distances = build_distances(points)
    inverse_index = {p: i for i, p in enumerate(points)}

    qu = QU(len(points))
    distances.sort(key=lambda d: d[0])

    i = 0
    d = None
    while qu.count > 1:
        d = distances[i]
        i += 1

        ai = inverse_index[d[1]]
        bi = inverse_index[d[2]]
        qu.union(ai, bi)

    if d:
        return d[1][0]*d[2][0]
    return 0

def eucl_dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    dz = abs(a[2] - b[2])

    return math.sqrt(sum(math.pow(x, 2) for x in (dx, dy, dz)))

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    points = [to_p(line) for line in lines]
    print(f'day8a: {solve_a(points)}')
    print(f'day8b: {solve_b(points)}')
