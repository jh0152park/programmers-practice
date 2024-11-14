import sys


w = int(sys.stdin.readline().strip())
l = int(sys.stdin.readline().strip())
h = int(sys.stdin.readline().strip())

if min(w, l) / h >= 2 and max(w, l) / min(w, l) <= 2:
    print("good")
else:
    print("bad")