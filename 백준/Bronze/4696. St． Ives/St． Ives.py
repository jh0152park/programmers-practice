import sys


while True:
    a = float(sys.stdin.readline().strip())
    if not a:
        break

    print("%.2f"%(a ** 4 + a ** 3 + a ** 2 + a ** 1 + a ** 0))