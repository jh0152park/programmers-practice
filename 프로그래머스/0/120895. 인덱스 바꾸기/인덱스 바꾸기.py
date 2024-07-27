def solution(my_string, num1, num2):
    string = ""
    
    for idx, str in enumerate(my_string):
        if idx == num1:
            string += my_string[num2]
        elif idx == num2:
            string += my_string[num1]
        else:
            string += str
            
    return string