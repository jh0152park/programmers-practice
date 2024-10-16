import heapq

def solution(scoville, K):
    s = []
    answer = 0
    
    for sco in scoville:
        heapq.heappush(s, sco)
    
    while len(s) > 1:
        lv1 = heapq.heappop(s)
        lv2 = heapq.heappop(s)
        
        if lv1 >= K:
            return answer
        
        answer += 1
        heapq.heappush(s, lv1 + (lv2 * 2))
        
    if not s or s[0] < K:
        return -1
    return answer