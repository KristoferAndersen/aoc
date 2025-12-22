def solve_a(fresh, available):
    total = 0
    i = 0
    for a in available:
        while i < len(fresh) and fresh[i][1] < a:
            i += 1

        if i == len(fresh):
            break

        if a >= fresh[i][0] and a <= fresh[i][1]:
            total += 1

    return total

def solve_b(fresh):
    return sum(b-a+1 for a, b in merged_ranges(fresh))

def merged_ranges(ranges):
    merged = []
    for lo, hi in ranges:
        if not merged or lo > merged[-1][1]:
            merged.append([lo, hi])
        else:
            merged[-1][1] = max(merged[-1][1], hi)

    return merged

if __name__ == '__main__':
    with open('input.txt') as f:
        fresh = []
        available = []

        target = fresh
        for line in f:
            line = line.strip()
            if line == '':
                target = available
                continue
            target.append(line)

        fresh = [tuple(map(int, f.split('-'))) for f in fresh]
        fresh = sorted(fresh, key=lambda l: l[0])
        available = sorted(int(a) for a in available)

        print('day5a:', solve_a(fresh, available))
        print('day5b:', solve_b(fresh))
