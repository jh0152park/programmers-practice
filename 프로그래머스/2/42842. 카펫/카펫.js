function solution(brown, yellow) {
    let total = brown + yellow;
    
    for(let x = total; x >= total / x; x--) {
        if(!(total % x)) {
            let y = total / x;
            
            if((x - 2) * (y - 2) === yellow) {
                return [x, y];
            }
        }
    }
}