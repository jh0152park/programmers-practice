n = int(input())
numbers = [int(input()) for _ in range(n)][::-1]
origin_numbers = numbers[::]


task = []
stack = []
my_numbers = []
number = 1
while numbers:
    target = numbers.pop()

    if not stack or stack[-1] < target: 
        for num in range(number, target + 1):
            stack.append(num)
            task.append("+")
        number = target + 1
        task.append("-")
        if not stack:
            break
        my_numbers.append(stack.pop())
    else:
        while stack:
            num = stack.pop()
            task.append("-")
            my_numbers.append(num)
            if num == target:
                break

if origin_numbers[::-1] != my_numbers:
    print("NO")
else:
    for c in task:
        print(c)