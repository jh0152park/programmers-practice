import sys


n = int(sys.stdin.readline().strip())

if n <= 100000 and not n % 2024:
    print("Yes")
else:
    print("No")