function get_gcd(u, v) {
    let t;
    while(v) {
        t = u % v;
        u = v;
        v = t;
    }
    return u;
}

function is_prime(n) {
    for(let i = 2; i <= Math.sqrt(n); i++) {
        if(n % i === 0) return false;
    }
    return true;
}


function solution(a, b) {
    
    if(a % b === 0) return 1;
    
    const gcd = get_gcd(a, b);
    let division = [];

    b /= gcd;
    
    for(let i = 2; i <= b; i++) {
        if(b % i === 0 && is_prime(i)) {
            division.push(i);
        }
    }
    
    division = division.join("")
    if(division === "2" || division === "5" || division === "25") return 1;
    
    return 2;
}