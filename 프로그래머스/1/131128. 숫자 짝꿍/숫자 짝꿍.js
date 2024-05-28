function solution(X, Y) {
    let common_numbers = [];
    let x_numbers = new Array(10).fill(0);
    let y_numbers = new Array(10).fill(0);
    
    
    for(let number of X) {
        x_numbers[+number]++;
    }
    
    for(let number of Y) {
        y_numbers[+number]++;
    }
    
    for(let i = 0; i < 10; i++) {
        if(x_numbers[i] > 0 && y_numbers[i]) {
            let cnt = x_numbers[i] > y_numbers[i] ? y_numbers[i] : x_numbers[i];
            for(let j = 0; j < cnt; j++) {
                common_numbers.push(i);
            }
        }
    }
    
    if(common_numbers.length === 0) {
        return "-1";
    }
    
    common_numbers = common_numbers.sort((a, b) => b - a);
    while(common_numbers.length > 1 && common_numbers[0] === 0) {
        common_numbers.shift();
    }
    
    return common_numbers.join("");
}