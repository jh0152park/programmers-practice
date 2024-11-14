import sys


bullet = 0
current_bullet = 0
n, k = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    action = sys.stdin.readline().strip()

    if action == "save":
        current_bullet = bullet
    elif action == "load":
        bullet = current_bullet
    elif action == "shoot":
        bullet -= 1
    elif action == "ammo":
        bullet += k

    print(bullet)