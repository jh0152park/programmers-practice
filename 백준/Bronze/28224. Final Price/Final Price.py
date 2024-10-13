import sys


n = int(sys.stdin.readline().strip())
cost = 0

for _ in range(n):
    cost += int(sys.stdin.readline().strip())
sys.stdout.write(f"{cost}")