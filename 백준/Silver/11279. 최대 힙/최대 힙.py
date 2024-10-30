import sys
import heapq


max_heap = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if num:
        heapq.heappush(max_heap, -num)
    else:
        if not max_heap:
            print("0")
        else:
            print(-heapq.heappop(max_heap))