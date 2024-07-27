def solution(num_list):
    odd = 0
    even = 0
    
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            odd += num_list[idx]
        else:
            even += num_list[idx]
            
    return odd if odd > even else even