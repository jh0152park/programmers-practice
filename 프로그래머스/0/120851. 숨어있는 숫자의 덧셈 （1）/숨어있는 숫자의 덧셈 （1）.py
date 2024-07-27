def solution(my_string):
    numbers = [str(i) for i in range(1, 10)]
    return sum([int(i) for i in my_string if i in numbers])