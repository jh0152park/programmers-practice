def solution(my_string):
    excepts = ("a", "e", "i", "o", "u")
    for i in excepts:
        my_string = my_string.replace(i, "")
    return my_string