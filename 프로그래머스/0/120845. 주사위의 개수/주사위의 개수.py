def solution(box, n):
    x = box[0] // n
    y = box[1] // n
    h = box[2] // n
    return x * y * h