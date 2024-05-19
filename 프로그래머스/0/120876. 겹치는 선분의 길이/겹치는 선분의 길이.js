function solution(lines) {
    var answer = 0;
    
    let cnts = [...Array(201).fill(0)];
    
    lines.forEach(line => {
        cnts[line[0] + 100]++;
        cnts[line[1] + 100]--;
    })
    
    for(let i = 1; i < 201; i++) {
        cnts[i] += cnts[i-1];
        if(cnts[i] > 1) answer++;
    }
    
    if(cnts[0] > 1) answer++;
    
    return answer;
}