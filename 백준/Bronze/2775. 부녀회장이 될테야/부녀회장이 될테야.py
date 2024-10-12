import sys
import pprint

tc = int(sys.stdin.readline().strip())

house = [[0] * 15 for _ in range(15)]

for i in range(15):
    house[0][i] = i + 1

for y in range(1, 15):
    for x in range(0, 15):
        house[y][x] = sum(house[y - 1][:x + 1])

for _ in range(tc):
    dong = int(sys.stdin.readline().strip())
    ho = int(sys.stdin.readline().strip())
    sys.stdout.write(f"{house[dong][ho-1]}\n")