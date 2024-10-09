lines = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

n = int(input())
flag = False
for _ in range(n):
    line = input().strip()
    if line not in lines:
        print("Yes")
        flag = True
        break

if not flag:
    print("No")
