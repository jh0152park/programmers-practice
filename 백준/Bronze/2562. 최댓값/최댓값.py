numbers = []
for _ in range(9):
    numbers.append(int(input()))

target = max(numbers)
print(target)
print(numbers.index(target) + 1)