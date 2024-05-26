function solution(cards1, cards2, goal) {
    for(let char of goal) {
        if(char === cards1[0] || char === cards2[0]) {
            if(char === cards1[0]) {
                cards1.shift();
                continue;
            } else {
                cards2.shift();
                continue;
            }
        }
        return "No";
    }
    
    return "Yes";
}