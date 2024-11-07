import sys


a, c, e = map(int, sys.stdin.readline().strip().split())
a_, c_, e_ = map(int, sys.stdin.readline().strip().split())

if a_ >= a and c_ >= c and e_ >= e:
    print("A")
elif a_ >= (a + 1) // 2 and c_ >= c and e_ >= e:
    print("B")
elif c_ >= c and e_ >= e:
    print("C")
elif c_ >= (c + 1) // 2 and e_ >= e:
    print("D")
else:
    print("E")