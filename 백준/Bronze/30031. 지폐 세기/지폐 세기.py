import sys


money = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000
}

n = int(sys.stdin.readline().strip())
total_money = 0
for _ in range(n):
    x, _ = map(int, sys.stdin.readline().strip().split())
    total_money += money[x]

print(total_money)