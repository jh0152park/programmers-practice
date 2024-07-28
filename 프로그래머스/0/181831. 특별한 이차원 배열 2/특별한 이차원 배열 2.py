def solution(arr):
    size = len(arr)
    
    for i in range(size):
        for j in range(size):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1