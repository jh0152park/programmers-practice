import sys


formula = sys.stdin.readline().strip().split()

if int(formula[0]) + int(formula[2]) == int(formula[-1]):
    print("YES")
else:
    print("NO")