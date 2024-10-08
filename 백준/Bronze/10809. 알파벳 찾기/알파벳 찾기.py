alpha = [-1] * 26
string = input().strip()


for i in range(len(string)):
    if alpha[ord(string[i]) - 97] == -1:
        alpha[ord(string[i]) - 97] = i

print(*alpha)