import sys


king = {
    "Lion": 0,
    "Tiger": 0
}
for _ in range(9):
    vote = sys.stdin.readline().strip()
    king[vote] += 1

print("Lion" if king["Lion"] > king["Tiger"] else "Tiger")