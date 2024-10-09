n = int(input())

cnt = 0
for _ in range(n):
    num = int(input())
    if num % 2:
        cnt += 1

print(cnt)