def solution(participant, completion):
    challenger = {}
    done = {}
    
    for player in participant:
        if not challenger.get(player):
            challenger[player] = 0
        challenger[player] += 1
        
    for player in completion:
        if not done.get(player):
            done[player] = 0
        done[player] += 1
        
    for player in challenger:
        if not done.get(player) or done[player] != challenger[player]:
            return player
