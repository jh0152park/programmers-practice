function solution(i, j, k) {
    var answer = 0;
    
    for(let z = i; z <= j; z++) {
        [...z.toString()].forEach(n => {
            if(+n === k) answer++;
        })
    }
    
    return answer;
}