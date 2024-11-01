import sys


a, b = map(int, sys.stdin.readline().strip().split())


if a == b:
    if a == 0:
        print("Not a moose")
    else:
        print(f"Even {a + b}")
elif a != b:
    print(f"Odd {max(a, b) * 2}")