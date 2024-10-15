def solution(nums):
    take = len(nums) // 2
    poketmon = list(set(nums))
    

    if take <= len(poketmon):
        return take
    
    return len(poketmon)
    