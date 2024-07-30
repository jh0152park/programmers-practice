def solution(s):
    letters = {}
    
    for c in s:
        if c not in letters.keys():
            letters[c] = 0
        letters[c] += 1
        
    str = []
    for c in letters.keys():
        if letters[c] == 1:
            str.append(c)
    
    return "".join(sorted(str))