import sys

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if not numbers:
        break
    print(sum(numbers))