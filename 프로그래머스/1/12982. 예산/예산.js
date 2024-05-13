function solution(d, budget) {
    var answer = 0;
    let left = budget;

    d.sort((a, b) => a - b);
    for(let i = 0; i < d.length; i++) {
        console.log(left);
        if(budget - d[i] >= 0) {
            answer++;
            budget -= d[i];
        } else {
            break;
        }
    }
    
    return answer;
}