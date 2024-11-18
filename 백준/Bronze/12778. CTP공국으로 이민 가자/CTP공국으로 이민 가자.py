import sys


alpha = [""]
for c in range(ord("A"), ord("Z") + 1):
    alpha.append(chr(c))

n = int(sys.stdin.readline().strip())
for _ in range(n):
    m, op = map(str, sys.stdin.readline().strip().split())
    questions = list(map(str, sys.stdin.readline().strip().split()))

    if op == "C":
        for question in questions:
            print(ord(question) - ord("A") + 1, end=" ")
    else:
        for question in questions:
            print(alpha[int(question)], end=" ")
    print("")