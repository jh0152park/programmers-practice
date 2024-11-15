import sys


while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline().strip()))

    for n in nums[::-1]:
        print(n)
    print(0)