function get_gcd(u, v) {
    let t;
    while (v) {
        t = parseInt(u % v)
        u = v
        v = t
    }
    return u;
}


function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    let parents = denom1 * denom2;
    let child = (numer1 * denom2) + (denom1 * numer2);
    let gcd = get_gcd(child, parents);
        
    return [parseInt(child/gcd), parseInt(parents/gcd)];
}