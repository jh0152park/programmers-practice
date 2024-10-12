import sys


n = int(sys.stdin.readline().strip())
numbers = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    numbers[num] += 1

for i in range(len(numbers)):
    num = numbers[i]
    if num:
        for j in range(num):
            sys.stdout.write(f"{i}\n")