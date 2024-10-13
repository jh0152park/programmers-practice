import sys


def check_brace(string):
    stack = []

    for c in string:
        if c == "(" or c == "[":
            stack.append(c)
        if c == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif c == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()

    if stack:
        return False
    return True


while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    if check_brace(string):
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")