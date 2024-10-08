n, m = map(int, input().split())
bucket = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    reverse = bucket[i-1:j][::-1]    
    for k in range(len(reverse)):
        bucket[i - 1 + k] = reverse[k]

print(*bucket)