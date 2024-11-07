import sys


a = 0
b = 0
front = ""
score = sys.stdin.readline().strip()

for i in range(0, len(score), 2):
    goal = int(score[i + 1])

    if score[i] == "A":
        a += goal
    else:
        b += goal

    if abs(a - b) >= 2 and front == "":
        if a > b:
            front = "A"
        else:
            front = "B"

    

if a == b:
    print(front)
else:
    if a > b:
        print("A")
    else:
        print("B")