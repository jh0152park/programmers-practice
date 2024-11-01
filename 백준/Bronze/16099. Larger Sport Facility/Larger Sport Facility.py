import sys


tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    tx, ty, ex, ey = map(int, sys.stdin.readline().strip().split())
    if tx * ty == ex * ey:
        print("Tie")  
    elif tx * ty > ex * ey:
        print("TelecomParisTech")
    else:
        print("Eurecom")