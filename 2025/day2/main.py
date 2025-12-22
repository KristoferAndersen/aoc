def solveA(ranges):
    total = 0
    for l, r in getBounds(ranges):
        for n in range(int(l), int(r)+1):
            if isRepeat(str(n)):
                total += n

    return total

def solveB(ranges):
    total = 0
    for l, r in getBounds(ranges):
        for n in range(int(l), int(r)+1):
            if isRepeatN(str(n)):
                total += n

    return total


def getBounds(ranges):
    return (s.split('-') for s in ranges)

def isRepeat(s):
    if len(s) % 2 != 0:
       return False

    i = 0
    j = len(s)//2
    while j < len(s):
        if s[i] != s[j]:
            return False
        j+=1
        i+=1

    return True

def isRepeatN(s):
    return len(s) > 1 and s in (s+s)[1:-1]

if __name__ == "__main__":
    with open('input.txt') as f:
        ranges = f.read().split(',')

        print("day2a:", solveA(ranges))
        print("day2b:", solveB(ranges))
