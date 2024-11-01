import sys


string = sys.stdin.readline().strip()

no = False
for letter in "MOBIS":
    if not string.count(letter):
        print("NO")
        no = True
        break

if not no:
    print("YES")