n = int(input())

print((n + 1) * n // 2)
print(((n + 1) * n // 2) ** 2)

sum = 0
for i in range(1, n + 1):
    sum += i ** 3

print(sum)