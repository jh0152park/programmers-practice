import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    suspect = sys.stdin.readline().strip()
    if "S" in suspect:
        print(suspect)
        break