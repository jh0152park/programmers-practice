n = int(input())
n_numbers = list(map(int, input().split()))
m = int(input())
m_numbers = list(map(int, input().split()))


numbers = {}
for num in n_numbers:
    numbers[num] = True

for num in m_numbers:
    if numbers.get(num):
        print("1")
    else:
        print("0")