import sys


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()


i = 0
detect = 0
pattern = 0

while i < m:
    if string[i:i+3] == "IOI":
        detect += 1
        i += 2
        if detect == n:
            pattern += 1
            detect -= 1
    else:
        i += 1
        detect = 0

print(pattern)