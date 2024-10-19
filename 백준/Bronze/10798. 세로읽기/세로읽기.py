import sys
import pprint


string = ""
letters = []
for _ in range(5):
    row = sys.stdin.readline().strip()
    row += " " * (15 - len(row))
    row = list(map(str, row))
    letters.append(row)

for i in range(15):
    for j in range(5):
        if letters[j][i] != " ":
            string += letters[j][i]

print(string)