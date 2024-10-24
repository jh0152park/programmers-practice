import sys



n, m = map(int, sys.stdin.readline().strip().split())
poketmon = [""] * (n + 1)

for i in range(1, n + 1):
    poketmon[i] = sys.stdin.readline().strip()
for i in range(m):
    q = sys.stdin.readline().strip()

    if q.isdigit():
        sys.stdout.write(f"{poketmon[int(q)]}\n")
    else:
        sys.stdout.write(f"{poketmon.index(q)}\n")