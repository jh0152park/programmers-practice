def solution(clothes):
    combi = 1
    closet = {}
    
    """
    1. 코니는 어떤 종류의 옷을 1벌이상 입을수도 있고 안입을 수도 있다.
       따라서 입지않는 경우까지 포함해야 하기에 amount + 1을 해서 경우의수를 곱한다.
    2. 마지막에 combi - 1을 하는 이유는
       코니는 최소 하루에 한개 이상의 옷을 입기 때문에 모든 종류를 하나도 입지않는
       즉, 나체의 경우의수를 제외해야하기 때문이다.
    """
    for cloth, category in clothes:
        if not closet.get(category):
            closet[category] = 0
        closet[category] += 1
        
    for category, amount in closet.items():
        combi *= (amount + 1)
    
    return combi - 1