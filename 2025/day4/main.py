def solve_a(grid):
    return sum(1 for _ in find_accessible(grid))

def solve_b(grid):
    scrolls = list(find_accessible(grid))
    for x, y in scrolls:
        grid[y][x] = 'x'

    if len(scrolls) == 0:
        return 0

    return len(scrolls) + solve_b(grid)

def find_accessible(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != '@':
                continue

            neighbor_scrolls = (1 for c2 in gen_neighbors(x, y, grid) if c2 == '@')
            if sum(neighbor_scrolls) < 4:
                yield (x, y)

def gen_neighbors(x, y, grid):
    offsets = [-1, 0, 1]
    for offset in offsets:
        x2 = x+offset
        for offset2 in offsets:
            y2 = y+offset2
            if (
                (offset == 0 and offset2 == 0)
                or x2 >= len(grid)
                or x2 < 0
                or y2 >= len(grid)
                or y2 < 0
            ):
                continue

            yield grid[y2][x2]

def gen_grid(f):
    return (list(l) for l in f)

if __name__ == '__main__':
    with open('input.txt') as f:
        grid = list(gen_grid(f))
        print('day3a:', solve_a(grid))
        print('day3b:', solve_b(grid))
