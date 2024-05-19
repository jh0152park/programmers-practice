function isPrime(n) {
    for(let i = 2; i <= Math.sqrt(n); i++) {
        if(n % i === 0) return false;
    }
    return true;
}

function solution(n) {
    var answer = [];
    let primes = [];
    
    for(let i = 2; i <= 10000; i++) {
        if(isPrime(i)) {
            primes.push(i);
        }
    }
    
    for(p of primes) {
        if(n % p === 0) answer.push(p)
    }
    

    
    return answer;
}