import sys


rage = 0
total_rage = 0
n = int(sys.stdin.readline().strip())
weather = list(map(int, sys.stdin.readline().strip().split()))

for w in weather:
    if w:
        rage += 1
    else:
        rage -= 1
    total_rage += rage

print(total_rage)