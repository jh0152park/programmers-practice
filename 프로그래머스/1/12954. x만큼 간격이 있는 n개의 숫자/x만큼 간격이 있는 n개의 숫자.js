function solution(x, n) {
    const gap = x;
    var answer = [];
    
    while(answer.length != n) {
        answer.push(x);
        x += gap;
    }
    
    return answer;
}