function get_gcd(u, v) {
    let t = 0;
    while(v) {
        t = u % v
        u = v
        v = t;
    }
    return u;
}

function solution(n) {
    let gcd = get_gcd(n, 6)
    return parseInt(n / gcd);
}