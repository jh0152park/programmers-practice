def create(num):
    base = num
    while num:
        base += num % 10
        num //= 10
    return base


n = int(input())
target = n

length = 0
while n:
    length += 1
    n //= 10

creater = 0
for num in range((10 ** (length - 1)) // 2, target):
    if create(num) == target:
        creater = num
        break

print(creater)