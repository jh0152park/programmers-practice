function solution(a, b, n) {
    let coke = 0;
    let left = 0;
    let answer = 0;
    
    while(n >= a) {
        left = n % a;
        coke = parseInt(n / a);
        n = coke * b + left;
        answer += coke * b;
    }
        
    return answer;
}
