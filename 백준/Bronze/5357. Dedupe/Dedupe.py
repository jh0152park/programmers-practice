import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    string = sys.stdin.readline().strip()
    stack = [string[0]]

    for s in string[1:]:
        if stack[-1] != s:
            stack.append(s)

    print("".join(stack))