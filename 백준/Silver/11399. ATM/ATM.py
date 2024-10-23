import sys


n = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))
times.sort()

psum = [0]
for i in range(n):
    psum.append(psum[-1] + times[i])

print(sum(psum))