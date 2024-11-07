import sys


n = int(sys.stdin.readline().strip())
for i in range(n):
    rice = list(map(int, sys.stdin.readline().strip().split()))
    print(f"Case #{i + 1}: {max(rice)}")