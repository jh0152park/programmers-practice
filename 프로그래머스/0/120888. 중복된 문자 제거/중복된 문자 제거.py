def solution(my_string):
    answer = []
    
    for s in my_string:
        if s not in answer:
            answer.append(s)
    
    return "".join(answer)