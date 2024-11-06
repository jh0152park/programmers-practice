import sys


def get_round(rank):
    if rank > 4500:
        return "Round 1"
    if rank > 1000:
        return "Round 2"
    if rank > 25:
        return "Round 3"
    return "World Finals"


n = int(sys.stdin.readline().strip())
for i in range(n):
    rank = int(sys.stdin.readline().strip())
    print(f"Case #{i + 1}: {get_round(rank)}")