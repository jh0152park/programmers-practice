import sys


b = int(sys.stdin.readline().strip())
p = 5 * b - 400

print(p)
if p < 100:
    print("1")
elif p > 100:
    print("-1")
else:
    print("0")