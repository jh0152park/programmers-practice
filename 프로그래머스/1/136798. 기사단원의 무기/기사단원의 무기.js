function get_divisor(number) {
    if(number === 1)    return 1;
    if(number === 2)    return 2;
    
    let divisors = [1];
    for(let i = 2; i <= Math.sqrt(number); i++) {
        if(!(number % i)) {
            divisors.push(i);
        }
    }
    
    let divisors2 = [];
    for(let divisor of divisors) {
        divisors2.push(number / divisor);
    }
    
    divisors = [...divisors, ...divisors2];
    divisors = Array.from(new Set(divisors));
    return divisors.length;
}

function solution(number, limit, power) {
    let iron = 0;
    
    for(let i = 1; i <= number; i++) {
        let divisor = get_divisor(i);
        
        if(divisor > limit) {
            iron += power;
        } else {
            iron += divisor;
        }
    }
    
    
    return iron;
}