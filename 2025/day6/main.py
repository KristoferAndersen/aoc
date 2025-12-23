import math

def solve_a(lines: list[str]):
    gens = (line.split() for line in lines[:-1])
    op_gen = iter(lines[-1].split())

    return sum((apply_op(nums, next(op_gen)) for nums in zip(*gens)))


def solve_b(lines: list[str]):
    gens = (iter(line) for line in lines[:-1])
    op_gen = iter(lines[-1].split())

    total = 0
    running = []
    for col in zip(*gens):
        tall_digits = [d for d in col if d is not None and d != ' ']
        tall_num = ''.join(tall_digits)

        if tall_num == '':
            total += apply_op(running, next(op_gen))
            running = []
        else:
            running.append(tall_num)


    total += apply_op(running, next(op_gen))

    return total

def apply_op(running, op):
    match op:
        case '+':
            return sum(int(n) for n in running)
        case '*':
            return math.prod(int(n) for n in running)
    return 0

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
    print('day6a:', solve_a(lines))
    print('day6b:', solve_b(lines))
