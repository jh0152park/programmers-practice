while 1:
    lines = list(map(int, input().split()))
    lines.sort()
    if sum(lines) == 0:
        break

    if (lines[0] ** 2) + (lines[1] ** 2) == lines[2] ** 2:
        print("right")
    else:
        print("wrong")