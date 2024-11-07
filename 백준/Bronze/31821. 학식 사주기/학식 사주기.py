import sys


menu = [0]
newbie = []

n = int(sys.stdin.readline().strip())
for _ in range(n):
    menu.append(int(sys.stdin.readline().strip()))

n = int(sys.stdin.readline().strip())
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    newbie.append(menu[m])

print(sum(newbie))