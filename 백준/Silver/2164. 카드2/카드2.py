from collections import deque

q = deque()
card = int(input())

for i in range(1, card + 1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])