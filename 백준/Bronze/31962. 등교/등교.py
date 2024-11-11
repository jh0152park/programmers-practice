import sys

"""
x분 이내로 도착해야함
n개의 버스 중 하나를 타야함
"""

def take_bus(bus, x):
    last = -1
    for s, t in bus:
        if s + t <= x:
            last = max(last, s)

    return last


bus = []
n, x = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    s, t = map(int, sys.stdin.readline().strip().split())
    bus.append((s, t))

print(take_bus(bus, x))