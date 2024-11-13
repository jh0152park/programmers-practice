import sys


n = int(sys.stdin.readline().strip())
lines = list(map(float, sys.stdin.readline().strip().split()))

volume = 0
for line in lines:
    volume += line ** 3

print(volume ** (1/3))