import sys


n = int(sys.stdin.readline().strip())
gift = 0

for _ in range(n):
    left = sys.stdin.readline().strip()
    if int(left.split("-")[-1]) <= 90:
        gift += 1
print(gift)