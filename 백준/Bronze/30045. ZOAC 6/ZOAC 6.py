import sys


emoji = 0
n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = sys.stdin.readline().strip()
    if "01" in s or "OI" in s:
        emoji += 1

print(emoji)