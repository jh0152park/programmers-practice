import sys


time = float("inf")
n = int(sys.stdin.readline().strip())

for _ in range(n):
    take, bread = map(int, sys.stdin.readline().strip().split())
    if take <= bread:
        time = min(time, bread)

if time == float("inf"):
    time = -1

print(time)