function solution(n) {
    let f = 1;
    let mul = 1;
    
    for(f = 1; f <= n; f++) {
        if(mul * f <= n) {
            mul *= f;
        } else {
            break;
        }
    }
    return --f;
}