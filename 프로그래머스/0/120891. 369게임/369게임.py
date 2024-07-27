def solution(order):
    nums = ["3", "6", "9"]
    return sum([1 for s in str(order) if s in nums])