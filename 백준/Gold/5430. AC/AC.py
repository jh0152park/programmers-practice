import sys
from collections import deque


def print_answer(answer):
    sys.stdout.write("[")
    for num in answer[:-1]:
        sys.stdout.write(f"{num},")
    sys.stdout.write(f"{answer[-1]}]\n")


tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    q = deque()
    error = False
    reverse = False
    
    cmd = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()

    if len(arr) == 2:
        arr = []
    else:
        arr = list(map(int, arr[1:-1].split(",")))

    q.extend(arr)
    for p in list(map(str, cmd)):
        if p == "R":
            reverse = not reverse
        else:
            if not q:
                error = True
                print("error")
                break
            else:
                if reverse:
                    q.pop()
                else:
                    q.popleft()
    if q:
        if reverse:
            print_answer(list(q)[::-1])
        else:
            print_answer(list(q))
    else:
        if not error:
            print([])