import sys

length = [0, 1, 1, 1, 2, 2]

for i in range(6, 101):
    length.append(length[-1] + length[-5])

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    sys.stdout.write(f"{length[n]}\n")