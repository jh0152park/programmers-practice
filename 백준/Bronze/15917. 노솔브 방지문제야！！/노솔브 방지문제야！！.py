import sys


q = int(sys.stdin.readline().strip())
possible = {}

for pow in range(32):
    possible[2 ** pow] = 1

for _ in range(q):
    a = int(sys.stdin.readline().strip())
    print(possible.get(a, 0))