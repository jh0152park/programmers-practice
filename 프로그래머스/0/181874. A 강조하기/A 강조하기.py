def solution(myString):
    return "".join([s.lower() for s in myString]).replace("a", "A")
    