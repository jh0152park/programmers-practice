import sys


"""
에스컬레이터 계단 21
일반 계단 17
"""

deepth = 0
while True:
    data = sys.stdin.readline().strip()
    if not data:
        break

    if data.split()[0] == "Es":
        deepth += int(data.split()[1]) * 21
    else:
        deepth += int(data.split()[1]) * 17

print(deepth)