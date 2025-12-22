def solveA(banks):
    total = 0
    for bank in banks:
        higher = max(enumerate(bank[:-1]), key=lambda t: t[1])
        lower = max(bank[higher[0]+1:])

        total += (int(higher[1])*10)+int(lower)

    return total

def solveB(banks):
    total = 0
    for bank in banks:
        joltage = 0
        for i in range(12):
            slice_len = len(bank) - (12 - i - 1)
            higher = max(enumerate(bank[:slice_len]), key=lambda t: t[1])
            bank = bank[higher[0]+1:]
            joltage = (joltage*10)+int(higher[1])

        total += joltage

    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        banks = f.read().splitlines()
        print("day3a:", solveA(banks))
        print("day3b:", solveB(banks))
