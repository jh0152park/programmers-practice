import sys


s = int(sys.stdin.readline().strip())
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

cost = 250
if a < s:
    cost += ((s - a) // b + 1 if (s - a) % b else (s - a) // b) * 100
print(cost)