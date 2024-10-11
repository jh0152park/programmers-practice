n = int(input())
cards = list(map(int, input().split()))
m = int(input())
my_cards = list(map(int, input().split()))

card_count = {}
for card in cards:
    if card_count.get(card):
        card_count[card] += 1
    else:
        card_count[card] = 1

for i in range(m):
    cnt = card_count.get(my_cards[i])
    if cnt:
        my_cards[i] = cnt
    else:
        my_cards[i] = 0

print(*my_cards)