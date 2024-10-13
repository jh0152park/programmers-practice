import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = sys.stdin.readline().strip()
    sys.stdout.write(f"{s.lower()}\n")