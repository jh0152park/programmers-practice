import sys


code = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
for _ in range(3):
    code.append(int(sys.stdin.readline().strip()))

number = 0
for i in range(len(code)):
    if i % 2:
        number += code[i] * 3
    else:
        number += code[i] * 1

print(f"The 1-3-sum is {number}")