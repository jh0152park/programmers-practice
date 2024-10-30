def max_fruit_length(n, fruits):
    left = 0
    max_length = 0
    fruit_count = {}
    
    for right in range(n):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        while len(fruit_count) > 2:
            fruit = fruits[left]
            fruit_count[fruit] -= 1
            if fruit_count[fruit] == 0:
                del fruit_count[fruit]
            left += 1
    
        max_length = max(max_length, right - left + 1)

    return max_length


n = int(input())
fruits = list(map(int, input().split()))
print(max_fruit_length(n, fruits))