def solution(a, d, included):
    return sum([i*d+a for i in range(len(included)) if included[i]])