import sys


n, b = map(str, sys.stdin.readline().strip().split())
b = int(b)

convert = 0
n = n[::-1]
for i in range(0, len(n)):
    if n[i].isdigit():
        convert += (b ** i) * int(n[i])
    else:
        convert += (b ** i) * ((ord(n[i]) - ord("A")) + 10)

print(convert)