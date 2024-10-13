import sys



n = int(sys.stdin.readline().strip())

numbers = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)
    

sys.stdout.write(f"{sum(numbers)}\n")