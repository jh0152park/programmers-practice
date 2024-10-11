def is_prime(num):
    if num < 2:
        return False
    n = 2
    while n ** 2 <= num:
        if num % n == 0:
            return False
        n += 1
    return True


n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for num in numbers:
    if is_prime(num):
        cnt += 1

print(cnt)