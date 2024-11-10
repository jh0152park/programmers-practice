import sys

a = 0
b = 0

string = sys.stdin.readline().strip()
for s in string:
    if s == "A":
        a += 1
    else:
        b += 1

print(f"{a} : {b}")