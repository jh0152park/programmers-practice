import sys


n = int(sys.stdin.readline().strip())
for i in range(1, n + 1):
    s = sys.stdin.readline().strip()
    print("%s%s"%(s, "" if s[-1] == "." else "."))