import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num % 2:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")