import sys


n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    numbers.append((x, y))

numbers.sort(key=lambda x:(x[1], x[0]))
for x, y in numbers:
    sys.stdout.write(f"{x} {y}\n")