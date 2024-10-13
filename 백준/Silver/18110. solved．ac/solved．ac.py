import sys
import math


n = int(sys.stdin.readline().strip())

numbers = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    numbers.append(num)

numbers.sort()
cut = math.floor((n * 0.15) + 0.5)

if n == 0:
    sys.stdout.write("0")
else:
    average = sum(numbers[cut:n-cut]) / (n - (cut * 2))
    average = math.floor(average + 0.5)
    sys.stdout.write(f"{average}")