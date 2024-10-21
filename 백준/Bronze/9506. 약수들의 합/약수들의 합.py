import sys


def is_perfect(num):
    sum = 0
    divs = []
    for n in range(1, num):
        if not num % n:
            sum += n
            divs.append(n)

    if sum == num:
        sys.stdout.write(f"{num} = ")
        for n in divs[:-1]:
            sys.stdout.write(f"{n} + ")
        sys.stdout.write(f"{divs[-1]}\n")
    else:
        sys.stdout.write(f"{num} is NOT perfect.\n")


while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break

    is_perfect(n)