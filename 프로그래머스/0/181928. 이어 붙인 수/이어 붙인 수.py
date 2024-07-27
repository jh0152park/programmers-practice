def list2num(num_list):
    mul = 1
    num = 0
    for n in range(len(num_list)-1, -1, -1):
        num += num_list[n] * mul
        mul *= 10
    return num

def solution(num_list):
    even = [n for n in num_list if n % 2 == 0]
    odd = [n for n in num_list if n % 2]
    return list2num(odd) + list2num(even)