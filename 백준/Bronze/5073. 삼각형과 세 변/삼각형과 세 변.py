import sys


while True:
    lines = sorted(list(map(int, sys.stdin.readline().strip().split())))
    if sum(lines) == 0:
        break

    if lines[0] + lines[1] <= lines[2]:
        print("Invalid")
    elif lines[0] == lines[2]:
        print("Equilateral")
    elif lines[0] != lines[1] and lines[1] != lines[2]:
        print("Scalene")
    else:
        print("Isosceles")