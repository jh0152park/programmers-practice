import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    odd = 0
    even = 0
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    for num in numbers[1:]:
        if num % 2:  odd += num
        else:        even += num
    print("ODD" if odd > even else "EVEN" if even > odd else "TIE")