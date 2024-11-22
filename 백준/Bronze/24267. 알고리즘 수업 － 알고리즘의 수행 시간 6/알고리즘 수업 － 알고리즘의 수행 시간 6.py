import sys


n = int(sys.stdin.readline().strip())

s = 0
for i in range(n - 2):
    s += (n - (i + 1)) * (n - (i + 2)) // 2

print(s)
print(3)