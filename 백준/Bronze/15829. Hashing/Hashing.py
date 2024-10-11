n = int(input())
str = input().strip()

sequence = []
for c in str:
    sequence.append(ord(c) - ord("a") + 1)

hash = 0
for i in range(n):
    hash += sequence[i] * (31 ** i)
print(hash % 1234567891)