def solution(arr):
    arr_len = len(arr)
    lengths = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    
    if arr_len in lengths:
        return arr
    
    for leng in lengths:
        if arr_len < leng:
            arr_len = leng - arr_len
            break

    for add in range(arr_len):
        arr.append(0)

    return arr
    