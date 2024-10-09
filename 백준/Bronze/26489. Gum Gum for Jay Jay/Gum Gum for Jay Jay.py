import sys

loop = 0
while True:
    data = sys.stdin.readline()
    if not data:
        break
    loop += 1
print(loop)