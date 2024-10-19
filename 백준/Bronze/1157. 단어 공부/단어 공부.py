import sys

alpha = [0] * 26
s = sys.stdin.readline().strip().lower()

for c in s:
    alpha[ord(c) - ord("a")] += 1


max_count = max(alpha)
max_index = alpha.index(max_count)
letter = chr(max_index + ord("a"))

alpha[max_index] = 0
max_count2 = max(alpha)

if max_count == max_count2:
    sys.stdout.write("?")
else:
    sys.stdout.write(letter.upper())