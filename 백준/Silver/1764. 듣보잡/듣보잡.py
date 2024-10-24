import sys


peoples = {}
unknown = []
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n + m):
    people = sys.stdin.readline().strip()
    
    if not people in peoples:
        peoples[people] = 0

    peoples[people] += 1
    if peoples[people] >= 2:
        unknown.append(people)

unknown.sort()
sys.stdout.write(f"{len(unknown)}\n")
for p in unknown:
    sys.stdout.write(f"{p}\n")