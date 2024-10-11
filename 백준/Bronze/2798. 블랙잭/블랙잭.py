n, m = map(int, input().split())
cards = list(map(int, input().split()))

card_sum = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                card_sum = max(card_sum, sum)

print(card_sum)