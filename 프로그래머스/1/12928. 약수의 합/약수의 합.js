function solution(n) {
    var answer = 1 + n;
    
    if(n <= 1) return n;

    for(let i = 2; i < n; i++) {
        if(!(n % i)) answer += i;
    }
    
    return answer;
}