import sys
import heapq

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    min_heap = []
    max_heap = []
    num_count = {}
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        oper, num = map(str, sys.stdin.readline().strip().split())
        num = int(num)
        if oper == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        else:
            if num == -1:
                while min_heap and num_count[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    smallest = heapq.heappop(min_heap)
                    num_count[smallest] -= 1
            else:
                while max_heap and num_count[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    largest = heapq.heappop(max_heap)
                    num_count[-largest] -= 1
    
    while min_heap and num_count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and num_count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        sys.stdout.write("EMPTY\n")
    else:
        sys.stdout.write(f"{-heapq.heappop(max_heap)} {heapq.heappop(min_heap)}\n")
