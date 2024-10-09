total = []
for _ in range(2):
    score = 0
    scores = list(map(int, input().split()))

    score += scores[0] * 6
    score += scores[1] * 3
    score += scores[2] * 2
    score += scores[3] * 1
    score += scores[4] * 2
    total.append(score)

print(*total)
