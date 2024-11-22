import sys


lines = sorted(list(map(int, sys.stdin.readline().strip().split())))

if lines[0] + lines[1] <= lines[2]:
    print((lines[0] + lines[1]) * 2 - 1)
elif lines[0] == lines[2]:
    print(lines[0] * 3)
else:
    print(sum(lines))