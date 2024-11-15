import sys


n = int(sys.stdin.readline().strip())
s = set(list(map(str, sys.stdin.readline().strip())))

print("Yes" if len(s) == 1 else "No")