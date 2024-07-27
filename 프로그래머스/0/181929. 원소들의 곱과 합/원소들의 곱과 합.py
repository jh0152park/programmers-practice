from functools import reduce

def solution(num_list):
    sum_ = sum(num_list)
    mul = reduce(lambda a, b: a * b, num_list, 1)
    
    return 1 if mul < sum_ ** 2 else 0