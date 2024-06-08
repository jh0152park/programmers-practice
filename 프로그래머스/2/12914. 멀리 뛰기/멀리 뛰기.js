function solution(n) {
    if(n <= 2) {
        return n;
    }
    
    let jump = new Array(n + 1).fill(1);
    
    for(let i = 2; i <= n; i++) {
        jump[i] = (jump[i - 1] + jump[i - 2]) % 1234567;
    }
        
    return jump[n];
}
