import sys

while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if not a and not b:
        break

    if not b % a:
        print("factor")
    elif not a % b:
        print("multiple")
    else:
        print("neither")