import heapq

def solution(jobs):
    # request time을 기준으로
    # 가장 먼저 요청한 task 순서로 정렬
    jobs.sort()
    
    heap = []
    task = len(jobs)
    completed = 0
    working_time = 0
    current_time = 0
    
    idx = 0
    while completed < task:
        # 정렬 완료된 jobs리스트를 조회하면서
        # 현재 시간을 기준으로 요청이 들어온 작업들을 선별
        while idx < task and jobs[idx][0] <= current_time:
            request_time, duration = jobs[idx]
            heapq.heappush(heap, (duration, request_time))
            idx += 1
            
        # 처리해야할 작업이 있다면.
        if heap:
            completed += 1
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            working_time += current_time - request_time
        else:
            current_time = jobs[idx][0]
            
    return working_time // task
            