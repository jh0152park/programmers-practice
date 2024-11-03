import sys

player = {
    0: "A", 1: "B", 2: "C"
}

zeroone = []
a, b, c = map(int, sys.stdin.readline().strip().split())
zeroone.append((a, 0))
zeroone.append((b, 1))
zeroone.append((c, 2))

zeroone.sort()


if zeroone[0][0] == zeroone[2][0]:
    print("*")
else:
    if zeroone[0][0] == zeroone[1][0]:
        print(player[zeroone[2][1]])
    else:
        print(player[zeroone[0][1]])