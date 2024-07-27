def solution(my_strings, parts):
    return "".join([my_strings[idx][part[0]:part[1]+1] for idx, part in enumerate(parts)])