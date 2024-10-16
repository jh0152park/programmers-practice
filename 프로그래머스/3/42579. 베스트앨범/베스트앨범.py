def solution(genres, plays):
    answer = []
    categories = {}
    play_count = []
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if not categories.get(genre):
            categories[genre] = {
                "total_play": 0,
                "play": []
            }
        categories[genre]["play"].append((play, i))
        categories[genre]["total_play"] += play
    
    for genre in categories.keys():
        play_count.append((categories[genre]["total_play"], genre))
        
    play_count.sort(key=lambda x:(-x[0]))
    print(play_count)
    
    for tplay, genre in play_count:
        categories[genre]["play"].sort(key=lambda x:-x[0])
        for play, idx in categories[genre]["play"][:2]:
            answer.append(idx)
    return answer
