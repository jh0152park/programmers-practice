def solution(num, k):
    nums = str(num)
    
    for i, s in enumerate(nums):
        if int(s) == k:
            return i + 1
    return -1