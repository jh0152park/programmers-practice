import sys


n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

dismatch = 0
for i in range(n):
    if s[i] != t[i]:
        dismatch += 1

print(dismatch)