import sys

def fact(num):
    fnum = 1
    for i in range(1, num + 1):
        fnum *= i
    return fnum

n = int(sys.stdin.readline().strip())
number = str(fact(n))[::-1]

cnt = 0
for n in number:
    if n == "0":
        cnt += 1
    else:
        break

sys.stdout.write(str(cnt))