import sys


n = int(sys.stdin.readline().strip())
track = list(map(str, sys.stdin.readline().strip().split()))
hellobit = sys.stdin.readline().strip()

print(track.count(hellobit))