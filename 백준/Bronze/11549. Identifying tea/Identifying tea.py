import sys

tea = int(sys.stdin.readline().strip())
answers = list(map(int, sys.stdin.readline().strip().split()))
print(answers.count(tea))