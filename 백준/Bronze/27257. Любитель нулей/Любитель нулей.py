import sys


s = str(int(sys.stdin.readline().strip()[::-1]))[::-1]
print(s.count("0"))