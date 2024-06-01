function solution(n) {
    let fibonacci = new Array(n + 1).fill(0);
    
    fibonacci[1] = 1;
    for(let i = 2; i <= n; i++) {
        fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 1234567;
    }
    
    return fibonacci[n];
}