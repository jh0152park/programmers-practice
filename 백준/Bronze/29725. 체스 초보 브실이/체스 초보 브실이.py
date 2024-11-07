import sys


white = 0
black = 0

property = {
    "k": 0,
    "p": 1,
    "n": 3,
    "b": 3,
    "r": 5,
    "q": 9
}

for _ in range(8):
    object = list(map(str, sys.stdin.readline().strip()))
    for obj in object:
        if obj != ".":
            if obj.islower():
                black += property[obj]
            else:
                white += property[obj.lower()]

print(white - black)