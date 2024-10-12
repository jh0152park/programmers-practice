import sys


peoples = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    weight, tall = map(int, sys.stdin.readline().strip().split())
    peoples.append([weight, tall, 0])


rank = []
for i in range(n):
    w = peoples[i][0]
    t = peoples[i][1]
    
    for j in range(n):
        if i != j:
            if peoples[j][0] > w and peoples[j][1] > t:
                peoples[i][2] += 1
    rank.append(peoples[i][2] + 1)

print(*rank)