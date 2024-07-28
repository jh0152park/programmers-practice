def solution(age):
    code = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return "".join([code[int(n)] for n in str(age)])