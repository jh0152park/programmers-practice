h, m = map(int, input().split())

# if h == 0:
#     h = 24

time = h * 60 + m
time -= 45

h = time // 60
m = time % 60

if h < 0:
    h = 23


print(h, m)