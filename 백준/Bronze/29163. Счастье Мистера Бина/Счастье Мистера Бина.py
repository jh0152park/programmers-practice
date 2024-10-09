n = int(input())
numbers = list(map(int, input().split()))

odd = 0
even = 0
for num in numbers:
    if num % 2:
        odd += 1
    else:
        even += 1

if even > odd:
    print("Happy")
else:
    print("Sad")