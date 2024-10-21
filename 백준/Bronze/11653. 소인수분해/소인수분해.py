import sys


priems = []
n = int(sys.stdin.readline().strip())

div = 2
while n > 1:
    if not n % div:
        priems.append(div)
        n //= div
    else:
        div += 1

for num in priems:
    print(num)