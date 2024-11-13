import sys


n = int(sys.stdin.readline().strip())
if n % 2:
    print("SciComLove"[::-1])
else:
    print("SciComLove")