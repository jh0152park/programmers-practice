function combinations(items, set) {
    if(set === 1) {
        return items.map((item) => [item]);
    }
    let results = [];
    items.forEach((item, index) => {
        let left = items.slice(index + 1);
        let comnination = combinations(left, set - 1);
        comnination.forEach((v) => results.push([item, ...v]));
    })
    return results;
}


function is_sum_zero(items) {
    return items[0] + items[1] + items[2] === 0 ? 1 : 0;
}


function solution(number) {
    let cnt = 0;
    let combination = combinations(number, 3);
        
    combination.forEach((combi) => {
        if(is_sum_zero(combi)) {
            cnt++;
        }
    })
    
    return cnt;
}