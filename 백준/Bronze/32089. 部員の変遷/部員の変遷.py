import sys


while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    students = list(map(int, sys.stdin.readline().strip().split()))
    max_student = float("-inf")
    for i in range(n - 2):
        max_student = max(max_student, sum(students[i:i+3]))

    print(max_student)