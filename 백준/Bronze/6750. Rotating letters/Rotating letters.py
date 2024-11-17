import sys


letters = {
    "I": True,
    "O": True,
    "S": True,
    "H": True,
    "Z": True,
    "X": True,
    "N": True
}

word = sys.stdin.readline().strip()
for s in word:
    if not letters.get(s):
        print("NO")
        exit(0)
print("YES")