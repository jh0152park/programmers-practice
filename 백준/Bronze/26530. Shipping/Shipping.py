import sys


n = int(sys.stdin.readline().strip())

for _ in range(n):
    total = 0
    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        data = sys.stdin.readline().strip().split()
        total += float(data[2]) * int(data[1])

    print("$%.2f"%(total))