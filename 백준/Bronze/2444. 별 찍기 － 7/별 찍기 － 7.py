import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    sys.stdout.write(" " * (n - i - 1))
    sys.stdout.write("*" * (i * 2 + 1))
    sys.stdout.write("\n")
for i in range(n - 1, 0, -1):
    sys.stdout.write(" " * (n - i))
    sys.stdout.write("*" * (i * 2 - 1))
    sys.stdout.write("\n")

