import sys


n = int(sys.stdin.readline().strip())
seven = 0

for _ in range(3):
    row = sys.stdin.readline().strip()
    if "7" in row:
        seven += 1

print("777" if seven == 3 else "0")