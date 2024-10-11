n = int(input())

members = []
for i in range(n):
    age, name = map(str, input().split())
    members.append((int(age), name, i))

members.sort(key=lambda x:(x[0], x[2]))
for age, name, i in members:
    print(age, name)