import sys


def right(dir):
    return (dir + 1) % 4
  

def left(dir):
    if dir == 0:
        return 3
    return dir - 1

def back(dir):
    return (dir + 2) % 4

# 0 north, 1 east, 2 south, 3 west
current = 0
dir = {
    0: "N",
    1: "E",
    2: "S",
    3: "W"
}
for _ in range(10):
    order = int(sys.stdin.readline().strip())
    if order == 1:
        current = right(current)
    elif order == 2:
        current = back(current)
    else:
        current = left(current)

print(dir[current])