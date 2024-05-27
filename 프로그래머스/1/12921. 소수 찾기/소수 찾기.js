function is_prime(num) {
    for(let i = 2; i <= Math.sqrt(num); i++) {
        if(!(num % i)) {
            return false;
        }
    }
    return true;
}


function solution(n) {
    let prime_num = 0;
    let prime_map = new Array(n + 1).fill(true);
    
    for(let i = 2; i <= Math.sqrt(n); i++) {
        if(prime_map[i]) {
            let mul = 2;
            while(i * mul <= n) {
                prime_map[i * mul++] = false;
            }
        }
    }
    
    for(let i = 2; i < prime_map.length; i++) {
        if(prime_map[i]) {
            prime_num++;
        }
    }
    
    return prime_num;
}