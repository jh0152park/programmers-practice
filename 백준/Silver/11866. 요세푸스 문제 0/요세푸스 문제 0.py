import sys

history = []
sequence = []
n, k = map(int, sys.stdin.readline().split())

numbers = []
for i in range(1, n + 1):
    numbers.append(i)

sequence.append(k)
numbers[k - 1] = 0


idx = k - 1
for i in range(n - 1):
    move = 0
    while True:
        if numbers[idx] != 0:
            move += 1

        if move == k:
            break
            
        idx += 1
        idx %= n
        
    sequence.append(numbers[idx])
    numbers[idx] = 0

sys.stdout.write("<")
for num in sequence[:-1]:
    sys.stdout.write(f"{num}, ")
sys.stdout.write(f"{sequence[-1]}>")