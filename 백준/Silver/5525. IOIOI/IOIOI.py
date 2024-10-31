import sys


def get_ioi(n):
    str = ""

    for i in range(n * 2 + 1):
        if i % 2:
            str += "O"
        else:
            str += "I"

    return str

n = int(sys.stdin.readline().strip())
str_length = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()

cnt = 0
ioi = get_ioi(n)
ioi_len = len(ioi)
for i in range(str_length - ioi_len + 1):
    if string[i:i+ioi_len] == ioi:
        cnt += 1

print(cnt)