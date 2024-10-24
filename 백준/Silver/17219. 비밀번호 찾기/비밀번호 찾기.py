import sys


passwords = {}
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    site, pw = map(str, sys.stdin.readline().strip().split())
    passwords[site] = pw
for _ in range(m):
    site = sys.stdin.readline().strip()
    sys.stdout.write(f"{passwords[site]}\n")