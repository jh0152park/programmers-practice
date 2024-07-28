def solution(arr, intervals):
    return [arr[i] for idx in intervals for i in range(idx[0], idx[1]+1)]