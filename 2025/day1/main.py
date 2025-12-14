def solve_a(input):
    pos = 50
    hits = 0
    for line in input:
        move = int(line[1:])
        if line[0] == 'R':
            pos += move
        elif line[0] == 'L':
            pos -= move

        pos = pos%100
        if pos == 0:
            hits += 1

    return hits

def solve_b(input):
    pos = 50
    hits = 0
    for line in input:
        wasZero = pos == 0
        move = int(line[1:])
        if line[0] == 'R':
            pos += move
            if pos >= 100:
                hits += abs(pos)//100

        elif line[0] == 'L':
            pos -= move
            if pos <= 0:
                hits += (abs(pos)//100)+1

                # Discount 1 when crossing from 0
                if wasZero:
                    hits -= 1

        pos = pos%100

    return hits

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
        print("day 1a:", solve_a(data))
        print("day 1b:", solve_b(data))

