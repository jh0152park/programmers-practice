import sys


numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()

print(numbers[1])