function fact(n) {
    if (n <= 1)
        return 1;
    
    let f = 1;
    for(let i = 1; i <= n; i++)
        f *= i;
    return f;
}

function solution(balls, share) {
    
    const nf = fact(balls);
    const nmf = fact(balls-share);
    const mf = fact(share)
    
    return Math.round(nf / (nmf*mf));
}