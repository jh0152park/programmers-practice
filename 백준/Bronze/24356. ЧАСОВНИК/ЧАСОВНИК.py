import sys


def convert2min(h, m):
    return h * 60 + m

t1, m1, t2, m2 = map(int, sys.stdin.readline().strip().split())

start = convert2min(t1, m1)
end = convert2min(t2, m2)

if end < start:
    end = convert2min(t2 + 24, m2)

print(end - start, (end - start) // 30)