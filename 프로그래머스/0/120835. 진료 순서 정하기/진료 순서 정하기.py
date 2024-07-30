def solution(emergency):
    answer = []
    er = emergency.copy()
    er.sort(reverse=True)
        
    for em in emergency:
        answer.append(er.index(em) + 1)

    return answer