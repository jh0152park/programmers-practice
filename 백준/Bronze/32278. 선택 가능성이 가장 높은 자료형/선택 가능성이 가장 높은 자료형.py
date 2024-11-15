import sys


n = int(sys.stdin.readline().strip())

if -2 ** 15 <= n <= 2 ** 15 - 1:
    print("short")
elif -2 ** 31 <= n <= 2 ** 31 - 1:
    print("int")
else:
    print("long long")