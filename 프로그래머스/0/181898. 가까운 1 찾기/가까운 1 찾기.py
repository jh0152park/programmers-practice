def solution(arr, idx):
    if not 1 in arr:
        return -1
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
        
    return -1