import sys


scoville = {
    "Poblano":	1500,
    "Mirasol":	6000,
    "Serrano":	15500,
    "Cayenne":	40000,
    "Thai":	75000,
    "Habanero":	125000,
}

total = 0
n = int(sys.stdin.readline().strip())
for _ in range(n):
    pepper = sys.stdin.readline().strip()
    total += scoville[pepper]

print(total)