import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    l = int(sys.stdin.readline().strip())
    sys.stdout.write("=" * l + "\n")