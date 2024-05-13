function solution(num) {
    let i = 0;
    var answer = 0;
    
    for(i = 0; i < 500; i++) {
        if(num === 1) break;
        
        if(!(num % 2)) {
            num /= 2;
        } else {
            num *= 3;
            num++;
        }
    }
    
    return i === 500 ? -1 : i;
}