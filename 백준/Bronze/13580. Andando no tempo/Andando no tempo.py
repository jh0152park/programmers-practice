import sys


years = list(map(int, sys.stdin.readline().strip().split()))
years.sort()

if years[0] == years[1] or years[1] == years[2]:
    print("S")
elif years[0] + years[1] == years[2]:
    print("S")
else:
    print("N")