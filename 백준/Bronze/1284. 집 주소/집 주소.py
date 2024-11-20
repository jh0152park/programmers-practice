import sys


widths = [3] * 10
widths[0] = 4
widths[1] = 2


while True:
    number = sys.stdin.readline().strip()
    
    if number == "0":
        break
    
    width = len(number) + 1

    for n in number:
        width += widths[int(n)]

    print(width)