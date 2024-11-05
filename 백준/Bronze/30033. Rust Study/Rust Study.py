import sys


n = int(sys.stdin.readline().strip())
plan = list(map(int, sys.stdin.readline().strip().split()))
done = list(map(int, sys.stdin.readline().strip().split()))

complete = 0
for i in range(n):
    if done[i] >= plan[i]:
        complete += 1

print(complete)