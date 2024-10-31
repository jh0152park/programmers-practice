import sys
import heapq


heap = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            sys.stdout.write("0\n")
        else:
            min_value = heapq.heappop(heap)
            sys.stdout.write(f"{min_value[1]}\n")
            
            # while heap and heap[0] == min_value:
            #     heapq.heappop(heap)