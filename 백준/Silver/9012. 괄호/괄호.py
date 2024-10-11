def is_correct(str):
    stack = []
    for c in str:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True


n = int(input())

for _ in range(n):
    str = input().strip()
    if is_correct(str):
        print("YES")
    else:
        print("NO")