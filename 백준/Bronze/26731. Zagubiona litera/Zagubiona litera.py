import sys


letter = [0] * 26
S = sys.stdin.readline().strip()

for s in S:
    letter[ord(s) - 65] = 1

print(chr(letter.index(0) + 65))