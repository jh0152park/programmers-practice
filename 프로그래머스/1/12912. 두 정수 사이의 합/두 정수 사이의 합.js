function solution(a, b) {
    var answer = 0;
    let from = a > b ? b : a;
    let to = a > b ? a : b;
    
    if(a === b) return a;
    
    for(let i = from; i <= to; i++) {
        answer += i;
    }
    
    return answer;
}