import sys

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    clothes = {}
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        item, category = map(str, sys.stdin.readline().strip().split())
        if not category in clothes:
            clothes[category] = 0
        clothes[category] += 1

    combination = 1
    for category in clothes:
        combination *= clothes[category] + 1
    sys.stdout.write(f"{combination - 1}\n")