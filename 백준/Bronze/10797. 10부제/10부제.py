target = int(input())
cars = list(map(int, input().split()))

cnt = 0
for car in cars:
    if target == car:
        cnt += 1

print(cnt)