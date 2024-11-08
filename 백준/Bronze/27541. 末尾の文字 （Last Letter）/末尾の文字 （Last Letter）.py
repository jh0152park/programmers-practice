import sys


n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

if s[-1] == "G":
    print(s[:-1])
else:
    print(f"{s}G")