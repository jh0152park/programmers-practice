numbers = list(map(int, input().split()))

front = numbers[0] * numbers[1]
rear = numbers[2] * numbers[3] * numbers[4]
print(front - rear)