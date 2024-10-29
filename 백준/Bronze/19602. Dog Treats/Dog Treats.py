import sys


S = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
L = int(sys.stdin.readline().strip())

happiness = (1 * S) + (2 * M) + (3 * L)
if happiness >= 10:
    print("happy")
else:
    print("sad")