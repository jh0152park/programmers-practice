def solution(num_list):
    odd = 0
    even = 0
    
    for n in num_list:
        if n % 2:   odd += 1
        else:       even += 1
    
    return [even, odd]