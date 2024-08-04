import math
from itertools import permutations


def perm2num(perm):
    nums = []
    for p in perm:
        nums.append(str(p))
    return int("".join(nums))
    

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
    
def solution(numbers):
    answer = 0
    already = {}
    numbers = list(map(int, list(numbers)))
    
    for num in range(1, len(numbers) + 1):
        for perm in permutations(numbers, num):
            each_num = perm2num(perm)
            if each_num not in already:
                already[each_num] = True
                if is_prime(each_num):
                    answer += 1
    
    return answer