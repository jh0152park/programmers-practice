import sys


n = int(sys.stdin.readline().strip())

print("Gnomes:")
for _ in range(n):
    gnome = list(map(int, sys.stdin.readline().strip().split()))
    order_gonme = gnome[::]
    order_gonme.sort()

    if order_gonme == gnome or order_gonme[::-1] == gnome:
        print("Ordered")
    else:
        print("Unordered")