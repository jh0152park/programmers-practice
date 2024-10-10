l, p = map(int, input().split())
news = list(map(int, input().split()))

for i in range(5):
    news[i] -= l * p

print(*news)