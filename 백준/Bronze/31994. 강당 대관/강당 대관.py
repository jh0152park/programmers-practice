import sys


to = 0
seminar = ""
while True:
    data = sys.stdin.readline().strip()
    if not data:
        break

    if int(data.split()[1]) > to:
        to = int(data.split()[1])
        seminar = data.split()[0]
print(seminar)