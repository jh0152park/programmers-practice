import sys


letter = ["h", "a", "b", "c", "d", "e", "f", "g"]

n = int(sys.stdin.readline().strip())

if n % 8:
    print(letter[n % 8] + str(n // 8 + 1))
else:
    print(letter[n % 8] + str(n // 8))