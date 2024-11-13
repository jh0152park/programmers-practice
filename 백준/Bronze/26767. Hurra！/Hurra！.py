import sys


n = int(sys.stdin.readline().strip())
for i in range(1, n + 1):
    if not i % 7 and i % 11:
        print("Hurra!")
    elif i % 7 and not i % 11:
        print("Super!")
    elif not i % 7 and not i % 11:
        print("Wiwat!")
    else:
        print(i)