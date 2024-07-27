def solution(str_list, ex):
    return "".join([str for str in str_list if not ex in str])