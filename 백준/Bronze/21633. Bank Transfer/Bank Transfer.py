import sys


fee = 25.00
money = int(sys.stdin.readline().strip())
fee += money * 0.01

fee = max(fee, 100)
fee = min(fee, 2000)

print("%.2f"%(fee))