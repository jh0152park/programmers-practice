function solution(n) {
    var answer = '';
    const str = ["수", "박"];
    
    for(let i = 0; i < n; i++) {
        answer += str[i % 2];
    }
    
    return answer;
}