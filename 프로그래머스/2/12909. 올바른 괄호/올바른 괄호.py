def solution(s):
    brace = []
    
    for c in s:
        if c == "(":
            brace.append(c)
        else:
            if not brace:
                return False
            if brace[-1] == ")":
                return False
            brace.pop()
    
    return True if not brace else False