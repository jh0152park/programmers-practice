students = [0] * 30
for i in range(28):
    student = int(input())
    students[student - 1] = 1

detect = []
for i in range(len(students)):
    if not students[i]:
        detect.append(i + 1)

detect.sort()
print(detect[0])
print(detect[1])