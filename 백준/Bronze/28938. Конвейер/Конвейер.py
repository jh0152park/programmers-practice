n = int(input())
belt = list(map(int, input().split()))

left = 0
right = 0

for move in belt:
    if move == -1:
        left += 1
    elif move == 1:
        right += 1

if left == right:
    print("Stay")
elif left > right:
    print("Left")
else:
    print("Right")