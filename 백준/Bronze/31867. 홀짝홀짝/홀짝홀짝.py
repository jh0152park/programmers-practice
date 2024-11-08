import sys


odd = 0
even = 0

_ = int(sys.stdin.readline().strip())
k = sys.stdin.readline().strip()

for n in k:
    if int(n) % 2:
        odd += 1
    else:
        even += 1

if even > odd:
    print("0")
elif odd > even:
    print("1")
else:
    print("-1")