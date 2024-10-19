import sys


n, b = map(int, sys.stdin.readline().strip().split())

bnum = ""
while n:
    mod = n % b

    if mod >= 10:
        bnum += chr(mod + 55)
    else:
        bnum += str(mod)
    
    n //= b

print(bnum[::-1])