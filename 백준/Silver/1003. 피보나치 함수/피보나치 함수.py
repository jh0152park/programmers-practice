import sys

dp_zero = [0] * 41
dp_one = [0] * 41

dp_zero[0] = 1
dp_one[0] = 0
dp_zero[1] = 0
dp_one[1] = 1

for i in range(2, 41):
    dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
    dp_one[i] = dp_one[i-1] + dp_one[i-2]

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    sys.stdout.write(f"{dp_zero[n]} {dp_one[n]}\n")