import sys

div_num = []
n, k = map(int, sys.stdin.readline().strip().split())

for d in range(1, n + 1):
    if not n % d:
        div_num.append(d)
    if len(div_num) > k:
        break

if len(div_num) < k:
    print("0")
else:
    print(div_num[k-1])