a, b, v = map(int, input().split())

day = (v - a) // (a - b)
if (v - a) % (a - b):
    day += 1
day += 1
print(day)