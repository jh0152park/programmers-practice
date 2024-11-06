import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    vote = int(sys.stdin.readline().strip())

    print("++++ " * (vote // 5), end="")
    print("|" * (vote % 5))