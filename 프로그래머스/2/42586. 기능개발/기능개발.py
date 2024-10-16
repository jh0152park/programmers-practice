from collections import deque


def solution(progresses, speeds):
    q = deque()
    s = deque()
    answer = []
    
    q.extend(progresses)
    s.extend(speeds)
    
    while q:
        while q[0] < 100:
            for i in range(len(s)):
                q[i] += s[i]
        
        print(q)
        cnt = 0
        while q and q[0] >= 100:
            cnt += 1
            q.popleft()
            s.popleft()
        answer.append(cnt)
    return answer