meat = int(input().strip())
target = int(input().strip())
c = int(input().strip())
d = int(input().strip())
e = int(input().strip())

time = 0

if meat < 0:
    time += abs(meat) * c
    meat = 0
if meat == 0:
    time += d
time += (target - meat) * e

print(time)