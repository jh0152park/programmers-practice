import sys


s = {}
m = int(sys.stdin.readline().strip())

for _ in range(m):
    data = list(map(str, sys.stdin.readline().strip().split()))

    if data[0] == "add":
        s[data[1]] = True
    elif data[0] == "remove" and data[1] in s and s[data[1]]:
        s[data[1]] = False
    elif data[0] == "check":
        if data[1] in s and s[data[1]]:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif data[0] == "toggle":
        if data[1] in s and s[data[1]]:
            s[data[1]] = False
        else:
            s[data[1]] = True
    elif data[0] == "all":
        for i in range(1, 21):
            s[str(i)] = True
    elif data[0] == "empty":
        s = {}