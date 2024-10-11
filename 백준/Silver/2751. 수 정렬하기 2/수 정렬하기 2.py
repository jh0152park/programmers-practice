import sys

n = int(sys.stdin.readline().strip())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))
numbers.sort()
for n in numbers:
    print(n)