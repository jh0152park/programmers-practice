n, m = map(int, input().split())
bucket = [0] * n

for _ in range(m):
    i, j, ball = map(int, input().split())
    for k in range(i, j + 1):
        bucket[k - 1] = ball

print(*bucket)