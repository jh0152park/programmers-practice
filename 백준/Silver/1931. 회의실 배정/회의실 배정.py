import sys


meeting_room = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    s, e = map(int, sys.stdin.readline().strip().split())
    meeting_room.append((s, e))

meeting_room.sort(key=lambda x:(x[1], x[0]))

book = 1
time = 0
for i in range(1, n):
    if meeting_room[time][1] <= meeting_room[i][0]:
        book += 1
        time = i
print(book)