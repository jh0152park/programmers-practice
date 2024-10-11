stack = []
n = int(input())

for _ in range(n):
    data = list(map(str, input().split()))
    if data[0] == "push":
        stack.append(data[1])
    if data[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    if data[0] == "size":
        print(len(stack))
    if data[0] == "empty":
        if stack:
            print(0)
        else:
            print("1")
    if data[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")