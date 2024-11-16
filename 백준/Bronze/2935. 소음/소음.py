import sys


a = int(sys.stdin.readline().strip())
op = sys.stdin.readline().strip()
b = int(sys.stdin.readline().strip())

print(a + b if op == "+" else a * b)