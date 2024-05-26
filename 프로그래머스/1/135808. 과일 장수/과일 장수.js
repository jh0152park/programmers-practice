function solution(k, m, score) {
    let cost = 0;
    let available = [];
        
    available = score.sort((a, b) => b - a);
        
    let min = 0;
    let apples = [];
    for(let apple of available) {
        apples.push(apple);
        
        if(apples.length === m) {
            min = Math.min(...apples);
            cost += min * m;   
            apples = [];
        }
    }
    
    return cost;
}