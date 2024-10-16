import heapq

def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
        
    for oper in operations:
        op = oper.split()[0]
        n = int(oper.split()[1])
        
        if not op:
            continue

        if op == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        else:
            if not max_heap or not min_heap:
                continue
            if n == -1:
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
                heapq.heapify(max_heap)
            else:
                max_value = -heapq.heappop(max_heap)
                min_heap.remove(max_value)
                heapq.heapify(min_heap)
    
    if not min_heap:
        return [0, 0]

    min_value = heapq.heappop(min_heap)
    max_value = -heapq.heappop(max_heap)
    return [max_value, min_value]