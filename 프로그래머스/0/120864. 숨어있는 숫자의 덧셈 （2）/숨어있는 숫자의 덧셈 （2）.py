def solution(my_string):
    answer = 0
    numbers = []
    
    for num in range(0, 10):
        numbers.append(str(num))
        
    string = ""
    my_string.replace(" ", "")
    for s in my_string:
        if s in numbers:
            string += s
        elif s not in numbers and len(string) > 0:
            answer += int(string)
            string = ""
    
    if len(string) > 0:
        answer += int(string)
    
    return answer