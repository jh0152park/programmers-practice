import sys


device, tall = map(int, sys.stdin.readline().strip().split())
least = list(map(int, sys.stdin.readline().strip().split()))

possible = 0
for cm in least:
    if tall >= cm:
        possible += 1

print(possible)