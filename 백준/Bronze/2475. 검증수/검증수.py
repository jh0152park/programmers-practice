sn = list(map(int, input().split()))

sum = 0
for n in sn:
    sum += n ** 2

print(sum % 10)