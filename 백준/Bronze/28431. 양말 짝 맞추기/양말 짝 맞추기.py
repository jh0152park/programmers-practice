import sys


socks = [0] * 10
for _ in range(5):
    socks[int(sys.stdin.readline().strip())] += 1

for i in range(10):
    if socks[i] and socks[i] % 2:
        print(i)