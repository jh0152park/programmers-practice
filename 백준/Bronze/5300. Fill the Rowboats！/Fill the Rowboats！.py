import sys


n = int(sys.stdin.readline().strip())
for i in range(1, n + 1):
    sys.stdout.write(f"{i} ")
    if not i % 6:
        sys.stdout.write(f"Go! ")
if i % 6:
    sys.stdout.write(f"Go! ")