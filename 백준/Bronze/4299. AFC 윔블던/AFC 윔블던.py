sum, sub = map(int, input().split())

a = (sum + sub) // 2
b = sum - a

score = sorted([a, b], reverse=True)

if score[0] < 0 or score[1] < 0:
    print("-1")
elif score[0] + score[1] != sum or score[0] - score[1] != sub:
    print("-1")
else:
    print(*score)