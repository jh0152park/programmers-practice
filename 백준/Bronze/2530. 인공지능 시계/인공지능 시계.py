h, m, s = map(int, input().split())
need = int(input())

s += need + (m * 60) + (h * 3600)
h = s // 3600 % 24
m = s % 3600 // 60
s = s % 3600 % 60

print(h, m, s)