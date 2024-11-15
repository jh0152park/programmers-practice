import sys


team1 = list(map(int, sys.stdin.readline().strip().split()))
team2 = list(map(int, sys.stdin.readline().strip().split()))

score1 = team1[0] + (team1[1] * 2) + (team1[2] * 3)
score2 = team2[0] + (team2[1] * 2) + (team2[2] * 3)

if score1 > score2:
    print("1")
elif score1 < score2:
    print("2")
else:
    print("0")