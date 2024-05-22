function combinations(items, set) {
    if(set === 1) {
        return items.map((item) => [item]);
    }
    
    let results = [];
    items.forEach((item, index) => {
        let left = items.slice(index + 1);
        let combination = combinations(left, set - 1);
        combination.forEach((combi) => results.push([item, ...combi]));
    })
    
    return results;
}


function solution(numbers) {
    var answer = [];
    let combination = combinations(numbers, 2);
    
    combination.forEach((combi) => answer.push(combi[0] + combi[1]));
    
    return Array.from(new Set(answer.sort((a, b) => a - b)));
}