def solution(intStrs, k, s, l):
    return [int(str[s:s+l]) for str in intStrs if int(str[s:s+l]) > k]