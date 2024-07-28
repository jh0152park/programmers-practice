def solution(a, b, c):
    dice = sorted([a, b, c])
    
    if dice[0] != dice[1] and dice[1] != dice[2]:
        return sum(dice)
    if dice[0] == dice[1] and dice[1] == dice[2]:
        return sum(dice) * (dice[0]**2 + dice[1]**2 + dice[2]**2) * (dice[0]**3 + dice[1]**3 + dice[2]**3)
    
    return sum(dice) * (dice[0]**2 + dice[1]**2 + dice[2]**2)