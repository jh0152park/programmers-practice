h, m = map(int, input().split())
w = int(input())

t = h * 60 + m + w
h = (t // 60) % 24
m = t % 60

print(h, m)