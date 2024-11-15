import sys


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = []

for i in range(len(a)):
    c.append(str(max(int(a[i]), int(b[i]))))

print("".join(c))