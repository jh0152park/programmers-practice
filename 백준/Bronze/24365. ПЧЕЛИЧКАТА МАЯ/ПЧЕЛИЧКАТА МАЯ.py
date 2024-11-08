import sys


bee = list(map(int, sys.stdin.readline().strip().split()))
avg = sum(bee) // 3

fly = 0
for i in range(2, -1, -1):
    if bee[i] > avg:
        bee[i-1] += bee[i] - avg
        fly += bee[i] - avg

print(fly)