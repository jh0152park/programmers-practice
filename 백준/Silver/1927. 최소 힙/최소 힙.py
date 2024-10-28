import sys
import heapq


heap = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if num:
        heapq.heappush(heap, num)
    else:
        if not heap:
            sys.stdout.write(f"{0}\n")
        else:
            sys.stdout.write(f"{heapq.heappop(heap)}\n")