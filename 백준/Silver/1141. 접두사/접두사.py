import sys


words = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)


words = list(set(words))
words.sort()
cnt = 0



for i in range(len(words)):
    include = False
    for j in range(i + 1, len(words)):
        word = words[i]
        if words[j][:len(word)] == word:
            include = True
            break
    if not include:
        cnt += 1

print(cnt)