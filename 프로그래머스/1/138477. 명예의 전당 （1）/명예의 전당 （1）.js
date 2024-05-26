function solution(k, score) {
    var answer = [];
    
    score.forEach((s, i) => {
        if(i < k) {
            answer.push(Math.min(...score.slice(0, i + 1)));
        } else {
            let rank = score.slice(0, i + 1).sort((a, b) => b - a);
            answer.push(rank[k - 1]);
        }
    })
    
    return answer;
}
