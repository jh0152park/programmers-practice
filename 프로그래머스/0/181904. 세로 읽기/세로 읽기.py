def solution(my_string, m, c):
    return "".join([my_string[s] for s in range(c - 1, len(my_string), m)])