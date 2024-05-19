function solution(emergency) {
    let answer = []
    let rank = [...emergency]
    
    rank.sort((a, b) => b - a);
    emergency.forEach(n => {
        answer.push(rank.indexOf(n)+1)
    })
    return answer;
}