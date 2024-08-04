from itertools import permutations


def hunt(current_hp, sequence, dungeons):
    clear = 0
    
    for i in sequence:
        need_hp, spent_hp = dungeons[i]
        if current_hp >= need_hp:
            clear += 1
            current_hp -= spent_hp
        else:
            break
            
    return clear
        


def solution(k, dungeons):
    sequences = permutations(list(range(len(dungeons))))
    
    max_clear = 0
    for sequence in sequences:
        clear = hunt(k, sequence, dungeons)
        max_clear = max(max_clear, clear)
    
    return max_clear