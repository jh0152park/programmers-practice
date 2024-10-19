import sys

n = int(sys.stdin.readline().strip())

check = 0
for _ in range(n):
    alpha = [0] * 26
    string = sys.stdin.readline().strip()

    fail = False
    for i in range(len(string)):
        s = string[i]
        idx = ord(s) - ord("a")
        
        if not alpha[idx]:
            alpha[idx] += 1
            continue
        else:
            if string[i-1] != s:
                fail = True
                break
            else:
                alpha[idx] += 1

    if not fail:
        check += 1

print(check)