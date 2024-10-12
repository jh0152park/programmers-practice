import sys

n = int(sys.stdin.readline().strip())

m = 0
number = 666
while True:
    if "666" in  str(number):
        m += 1
        if n == m:
            break
    number += 1

sys.stdout.write(str(number))