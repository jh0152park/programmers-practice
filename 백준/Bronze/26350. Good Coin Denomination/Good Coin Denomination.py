import sys


n = int(sys.stdin.readline().strip())

for _ in range(n):
    bad = False
    coins = list(map(int, sys.stdin.readline().strip().split()[1:]))
    
    coin = coins[0]
    for c in coins[1:]:
        if not c >= coin * 2:
            bad = True
            break
        coin = c

    print("Denominations: ", end="")
    print(*coins)
    print("%s coin denominations!\n"%("Bad" if bad else "Good"))