import sys
import math


numbers = []
numbers_count = {}
n = int(sys.stdin.readline().strip())

if n == 1:
    num = int(sys.stdin.readline().strip())
    sys.stdout.write(f"{num}\n")
    sys.stdout.write(f"{num}\n")
    sys.stdout.write(f"{num}\n")
    sys.stdout.write(f"0\n")
else:
    for _ in range(n):
        numbers.append(int(sys.stdin.readline().strip()))
        if numbers_count.get(numbers[-1]):
            numbers_count[numbers[-1]] += 1
        else:
            numbers_count[numbers[-1]] = 1
    
    numbers.sort()
    
    counts = []
    for num in numbers_count.keys():
        counts.append((num, numbers_count[num]))
    
    counts.sort(key=lambda x:(-x[1], x[0]))
    
    ret = counts[0][0]
    if counts[0][1] == counts[1][1]:
        ret = counts[1][0]
    
    sys.stdout.write(f"{math.floor((sum(numbers) / n) + 0.5)}\n")
    sys.stdout.write(f"{numbers[n // 2]}\n")
    sys.stdout.write(f"{ret}\n")
    sys.stdout.write(f"{numbers[-1] - numbers[0]}\n")