import sys


def get_grade(rank, n):
    p = (rank * 100) // n

    if 0 <= p <= 4:    return 1
    if 4 < p <= 11:    return 2
    if 11 < p <= 23:    return 3
    if 23 < p <= 40:    return 4
    if 40 < p <= 60:    return 5
    if 60 < p <= 77:    return 6
    if 77 < p <= 89:    return 7
    if 89 < p <= 96:    return 8
    return 9


n, k = map(int, sys.stdin.readline().strip().split())
grade = list(map(int, sys.stdin.readline().strip().split()))

for i in range(k):
    grade[i] = get_grade(grade[i], n)

print(*grade)