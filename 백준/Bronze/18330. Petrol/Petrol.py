import sys


gasoline = int(sys.stdin.readline().strip())
left = int(sys.stdin.readline().strip()) + 60

if gasoline - left < 0:
    print(gasoline * 1500)
else:
    cost = (gasoline - left) * 3000
    cost += left * 1500
    print(cost)