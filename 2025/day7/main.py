def solve_a(lines):
    beams = set()
    for i, c in enumerate(lines[0]):
        if c == 'S':
            beams.add(i)

    splits = 0
    for line in lines[1:]:
        next_beams = set()
        for i in beams:
            if line[i] == '^':
                splits += 1
                if i != 0:
                    next_beams.add(i-1)
                if i != len(line)-1:
                    next_beams.add(i+1)
            else:
                next_beams.add(i)
        beams = next_beams

    return splits

def solve_b(lines):
    beams = {}
    for i, c in enumerate(lines[0]):
        if c == 'S':
            beams[i] = 1

    for line in lines[1:]:
        next_beams = {}
        for i in beams:
            if line[i] == '^':
                if i != 0:
                    next_beams[i-1] = next_beams.get(i-1, 0) + beams.get(i)
                if i != len(line)-1:
                    next_beams[i+1] = next_beams.get(i+1, 0) + beams.get(i)
            else:
                next_beams[i] = next_beams.get(i, 0) + beams.get(i, 0)
        beams = next_beams

    print(beams)
    return sum(beams[k] for k in beams)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
    print('day7a:', solve_a(lines))
    print('day7b:', solve_b(lines))
