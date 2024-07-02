function solution(want, number, discount) {
    var answer = 0;
    let bucket = {};
    let total_product = 0;
    
    for(let i = 0; i < want.length; i++) {
        total_product += number[i];
        bucket[want[i]] = number[i];
    }
    
    
    for(let i = 0; i <= discount.length - total_product; i++ ) {
        let not_mine = false;
        let should_buy = {...bucket};
        for(let j = i; j < i + total_product; j++) {
            let product = discount[j];
            
            if(!(!!should_buy[product])) {
                not_mine = true;
                break;
            }
            
            should_buy[product]--;
        }
                
        if(!not_mine) {
            const left = Object.values(should_buy).reduce((acc, cur) => acc + cur);
            if(!left) answer++;
        }
    }
    
    return answer;
}
