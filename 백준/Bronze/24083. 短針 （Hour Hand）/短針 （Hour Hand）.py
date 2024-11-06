import sys


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
print(f"{(a + b) % 12 if (a + b) % 12 else 12}")