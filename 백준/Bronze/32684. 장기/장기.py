import sys


units = {
    0: 13, 1: 7, 2: 5,
    3: 3, 4: 3, 5: 2
}

green = list(map(int, sys.stdin.readline().strip().split()))
red = list(map(int, sys.stdin.readline().strip().split()))

green_score = 0
red_score = 1.5

for i in range(6):
    green_score += units[i] * green[i]
    red_score += units[i] * red[i]

print("cocjr0208" if green_score > red_score else "ekwoo")