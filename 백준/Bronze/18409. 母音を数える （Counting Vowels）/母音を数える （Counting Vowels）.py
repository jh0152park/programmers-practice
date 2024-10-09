targets = ["a", "i", "u", "e", "o"]

n = int(input())
str = input().strip()

cnt = 0
for c in str:
    if c in targets:
        cnt += 1

print(cnt)