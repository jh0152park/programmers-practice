import sys

word = sys.stdin.readline().strip()
print(ord(word) - ord("가") + 1)