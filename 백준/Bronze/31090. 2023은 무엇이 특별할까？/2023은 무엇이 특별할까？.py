import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    year = int(sys.stdin.readline().strip())
    if not (year + 1) % (year % 100):
        print("Good")
    else:
        print("Bye")