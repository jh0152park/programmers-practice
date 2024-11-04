import sys

beef, cheese = map(int, sys.stdin.readline().strip().split())

if cheese >= beef - 1:
    print(beef * 2 - 1)
else:
    print(cheese * 2 + 1)