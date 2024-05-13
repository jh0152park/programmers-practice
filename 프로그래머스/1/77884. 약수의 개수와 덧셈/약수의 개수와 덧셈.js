function compute_divisor_number(number) {
    let count = 2;
    for(let i = 2; i < number; i++) {
        if(!(number % i)) {
            count++;
        }
    }
    return number === 1 ? 1 : count;
}

function solution(left, right) {
    var answer = 0;
    
    for(let i = left; i <= right; i++) {
        let div = compute_divisor_number(i);
        
        if(!(div % 2)) { // even
            answer += i;
        } else { // odd
            answer += -i;
        }
    }
    
    return answer;
}