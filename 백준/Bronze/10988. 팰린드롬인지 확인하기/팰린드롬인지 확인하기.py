import sys

s = sys.stdin.readline().strip()

if s == s[::-1]:
    sys.stdout.write("1")
else:
    sys.stdout.write("0")