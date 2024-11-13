import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    lens = list(map(int, sys.stdin.readline().strip().split()))
    print(*lens)
    
    lens.sort()
    if lens[0] >= 10:
        print("triple-double\n")
    elif lens[1] >= 10:
        print("double-double\n")
    elif lens[2] >= 10:
        print("double\n")
    else:
        print("zilch\n")