def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # H-Index를 찾기 위한 순차적 탐색
    # [6, 5, 3, 1, 0]
    for i, citation in enumerate(citations):
        # i는 현재 논문의 순번 (0-based index), citation은 인용 횟수
        # h번 이상 인용된 논문이 h편 이상이면 h-index가 됨
        if citation <= i:
            return i  # 인용된 논문 수가 h를 넘지 못할 때 i가 H-Index가 됨
    
    # 모든 논문이 h번 이상 인용된 경우, 전체 논문의 수가 H-Index
    return len(citations)
