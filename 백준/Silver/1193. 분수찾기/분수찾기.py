import sys
import bisect


numbers = [0]
for n in range(1, 10 ** 4):
    num = int((n * (n + 1)) * 0.5)
    numbers.append(num)
    if numbers[-1] > 10 ** 7:
        break


n = int(sys.stdin.readline().strip())
n_diagonal = bisect.bisect_left(numbers, n)
num = n_diagonal + 1
start_n = numbers[n_diagonal - 1] + 1


if n_diagonal % 2:
    son = n_diagonal
    mom = 1
else:
    son = 1
    mom = n_diagonal

while True:
    if start_n == n:
        print(f"{son}/{mom}")
        break
        
    if n_diagonal % 2:
        son -= 1
        mom += 1
    else:
        son += 1
        mom -= 1

    start_n += 1
    