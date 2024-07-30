def solution(num_list, n):
    nums = []
    answer = []
    
    for num in num_list:
        nums.append(num)
        if len(nums) == n:
            answer.append(nums)
            nums = []
    
    return answer