import sys


n = int(sys.stdin.readline().strip())
for i in range(n):
    players = {}
    backnumber = list(map(int, sys.stdin.readline().strip().split()))

    for b in backnumber:
        players[b] = True

    print(*backnumber)    
    if not players.get(18) and not players.get(17):
        print("none\n")
    elif players.get(18) and players.get(17):
        print("both\n")
    elif players.get(18) and not players.get(17):
        print("mack\n")
    else:
        print("zack\n")