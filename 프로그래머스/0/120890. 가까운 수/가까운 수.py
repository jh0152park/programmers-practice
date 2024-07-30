def solution(array, n):
    delta = []
    array.sort()
    
    for num in array:
        delta.append(abs(n - num))
    
    return array[delta.index(min(delta))]