import sys


options = [
    [1, 3],
    [6, 8],
    [2, 5],
]

for i in range(3):
    op = int(sys.stdin.readline().strip())
    if not op in options[i]:
        print("EI")
        exit(0)
print("JAH")