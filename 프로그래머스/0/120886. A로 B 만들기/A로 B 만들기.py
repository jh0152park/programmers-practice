def solution(before, after):
    before_sum = 0
    after_sum = 0
    
    for i in range(len(before)):
        before_sum += ord(before[i])
        after_sum += ord(after[i])

    return 1 if before_sum == after_sum else 0