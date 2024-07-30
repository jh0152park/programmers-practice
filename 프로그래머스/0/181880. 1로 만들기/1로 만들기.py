def is_odd(num):
    return num % 2

def convert_to_1(num):
    cnt = 0
    while num != 1:
        cnt += 1
        if is_odd(num):
            num -= 1
            num //= 2
        else:
            num //= 2
    return cnt

def solution(num_list):
    answer = 0
    
    for num in num_list:
        answer += convert_to_1(num)
    
    return answer