import sys

k, d, a = map(int, sys.stdin.readline().strip().split("/"))

if d == 0 or k + a < d:
    sys.stdout.write("hasu\n")
else:
    sys.stdout.write("gosu\n")