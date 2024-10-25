import sys


ways = [0, 1, 3]
n = int(sys.stdin.readline().strip())

for i in range(3, n + 1):
    ways.append((ways[i-2] * 2 + ways[i-1]) % 10007)

sys.stdout.write(f"{ways[n]}")