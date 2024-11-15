import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    balloons = sys.stdin.readline().strip()
    a = balloons.count("a")
    b = balloons.count("b")
    print(min(a, b))