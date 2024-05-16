function solution(num, total) {
    var answer = [];
    let d = 0;
    let start = 0;
    
    for(let i = 1; i < num; i++)
        d += i;
    
    start = parseInt((total - d) / num)
    
    
    for(let i = start; i < start + num; i++)
        answer.push(i)
    
    return answer;
}