import sys


n = int(sys.stdin.readline().strip())
call = list(map(int, sys.stdin.readline().strip().split()))

y = 0
m = 0

for i in range(n):
    y += ((call[i] // 30) + 1) * 10
    m += ((call[i] // 60) + 1) * 15

if y == m:
    print(f"Y M {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y {y}")