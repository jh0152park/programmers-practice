import sys


tc = 0
while True:
    tc += 1
    nums = list(map(int, sys.stdin.readline().strip().split()))

    if nums[0] == 0:
        break

    n = nums[0]
    d = nums[1:]

    print("Case %d: %.1f"%(tc, d[(n + 1)//2-1] if n % 2 else (d[n//2] + d[n//2-1]) / 2))
