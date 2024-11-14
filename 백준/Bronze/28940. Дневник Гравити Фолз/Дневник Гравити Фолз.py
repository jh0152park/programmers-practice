import sys


w, h = map(int, sys.stdin.readline().strip().split())
n, a, b = map(int, sys.stdin.readline().strip().split())

if a > w or b > h:
    print("-1")
else:
    page = w // a
    page *= h // b

    if n % page:
        print(n // page + 1)
    else:
        print(n // page)