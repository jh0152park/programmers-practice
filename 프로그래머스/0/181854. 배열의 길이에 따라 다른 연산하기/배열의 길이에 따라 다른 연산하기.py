def solution(arr, n):
    length = len(arr)
    
    if length % 2:
        return [num + n if not idx % 2 else num for idx, num in enumerate(arr)]
    
    return [num + n if idx % 2 else num for idx, num in enumerate(arr)]
        