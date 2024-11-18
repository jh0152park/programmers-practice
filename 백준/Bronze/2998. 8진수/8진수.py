import sys


num = sys.stdin.readline().strip()
print(oct(int(num, 2))[2:])