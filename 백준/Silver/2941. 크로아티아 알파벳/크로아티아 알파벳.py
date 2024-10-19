import sys


words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = sys.stdin.readline().strip()

word_count = 0
for word in words:
    cnt = string.count(word)
    string = string.replace(word, "-")
    word_count += cnt

print(word_count + len(string) - string.count("-"))