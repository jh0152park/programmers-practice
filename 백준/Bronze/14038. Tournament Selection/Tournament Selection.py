import sys


win = 0
lose = 0
for _ in range(6):
    result = sys.stdin.readline().strip()
    if result == "L":
        lose += 1
    else:
        win += 1

group = 0
if lose == 6:
    print("-1")
else:
    if win >= 5:
        print("1")
    elif win >= 3:
        print("2")
    else:
        print("3")