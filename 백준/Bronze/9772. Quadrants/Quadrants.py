import sys


while True:
    x, y = map(float, sys.stdin.readline().strip().split())

    if not x and not y:
        print("AXIS")
        break
    if not x or not y:
        print("AXIS")
    else:
        if x > 0 and y > 0:
            print("Q1")
        elif x < 0 and y > 0:
            print("Q2")
        elif x < 0 and y < 0:
            print("Q3")
        else:
            print("Q4")
    