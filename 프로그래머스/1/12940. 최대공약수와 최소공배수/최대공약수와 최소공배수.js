function get_gcd(n, m) {
    if(n < 0 || m < 0) {
        return 0;
    }
    
    let t;
    while(m) {
        t = n % m;
        n = m;
        m = t;
    }
    return n;
}



function solution(n, m) { 
    const gcd = get_gcd(n, m);
    return [gcd, n * m / gcd];
}