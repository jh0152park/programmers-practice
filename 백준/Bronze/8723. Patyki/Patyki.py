import sys



sticks = list(map(int, sys.stdin.readline().strip().split()))
sticks.sort()

if sticks[0] ** 2 + sticks[1] ** 2 == sticks[2] ** 2:
    print("1")
elif sticks[0] == sticks[1] and sticks[1] == sticks[2]:
    print("2")
else:
    print("0")