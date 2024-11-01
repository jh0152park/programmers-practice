import sys


emoji = sys.stdin.readline().strip()
complex = 0

complex += emoji.count("_") * 5
complex += len(emoji) + 2

print(complex)